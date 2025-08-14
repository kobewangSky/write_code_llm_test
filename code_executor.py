"""
Code execution and result comparison module
Safely execute LLM-generated code and compare results
"""
import subprocess
import tempfile
import logging
import time
import os
import re
from typing import Tuple, Optional, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)

class CodeExecutor:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        logger.info(f"Initializing code executor: timeout={timeout}s")
    
    def extract_python_code(self, llm_response: str) -> Optional[str]:
        """Extract Python code from LLM response"""
        if not llm_response:
            return None
        
        # Try to find ```python code blocks
        python_block_pattern = r'```python\s*\n(.*?)\n```'
        matches = re.findall(python_block_pattern, llm_response, re.DOTALL)
        
        if matches:
            logger.debug("Found Python code block")
            return matches[0].strip()
        
        # Try to find ``` code blocks
        code_block_pattern = r'```\s*\n(.*?)\n```'
        matches = re.findall(code_block_pattern, llm_response, re.DOTALL)
        
        if matches:
            logger.debug("Found code block")
            return matches[0].strip()
        
        # If no code blocks found, check if the entire response is code
        lines = llm_response.strip().split('\n')
        if any(line.strip().startswith(('def ', 'class ', 'import ', 'from ')) for line in lines):
            logger.debug("Treating entire response as code")
            return llm_response.strip()
        
        logger.warning("Unable to extract code from LLM response")
        return None
    
    def execute_code(self, code: str, input_data: str = "") -> Tuple[bool, str, str]:
        """
        Execute Python code
        Returns: (success, stdout, stderr)
        """
        if not code:
            return False, "", "Code is empty"
        
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_file = f.name
            
            logger.debug(f"Executing code file: {temp_file}")
            
            # Execute code
            process = subprocess.Popen(
                ['python', temp_file],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate(input=input_data, timeout=self.timeout)
            
            success = process.returncode == 0
            
            if success:
                logger.debug("Code execution successful")
            else:
                logger.warning(f"Code execution failed: return_code={process.returncode}")
            
            return success, stdout.strip(), stderr.strip()
            
        except subprocess.TimeoutExpired:
            logger.error(f"Code execution timeout ({self.timeout}s)")
            return False, "", f"Execution timeout ({self.timeout}s)"
        
        except Exception as e:
            logger.error(f"Code execution exception: {e}")
            return False, "", str(e)
        
        finally:
            # Clean up temporary file
            try:
                if 'temp_file' in locals():
                    os.unlink(temp_file)
            except:
                pass
    
    def execute_function(self, code: str, function_name: str = "solve", test_input: str = "") -> Tuple[bool, str, str]:
        """
        Execute specific function
        """
        if not code:
            return False, "", "Code is empty"
        
        # Create test code
        test_code = f"""
{code}

# Execute function
if __name__ == "__main__":
    try:
        if '{function_name}' in globals():
            result = {function_name}("{test_input}")
            print(result)
        else:
            print("ERROR: Function {function_name} not found")
    except Exception as e:
        print(f"ERROR: {{e}}")
"""
        
        return self.execute_code(test_code)
    
    def compare_results(self, actual: str, expected: str, comparison_mode: str = "exact") -> bool:
        """
        Compare execution results with expected answer
        comparison_mode: "exact", "normalize", "code_comparison"
        """
        if not actual or not expected:
            return False
        
        actual = actual.strip()
        expected = expected.strip()
        
        if comparison_mode == "exact":
            return actual == expected
        
        elif comparison_mode == "normalize":
            # Normalized comparison: ignore spaces, newlines, etc.
            actual_norm = re.sub(r'\s+', ' ', actual.lower())
            expected_norm = re.sub(r'\s+', ' ', expected.lower())
            return actual_norm == expected_norm
        
        elif comparison_mode == "code_comparison":
            # Code comparison: compare functionality rather than strings
            try:
                return self._compare_code_functionality(actual, expected)
            except:
                return self.compare_results(actual, expected, "normalize")
        
        return False
    
    def _compare_code_functionality(self, code1: str, code2: str) -> bool:
        """Compare if two pieces of code have the same functionality"""
        # More complex code functionality comparison logic can be implemented here
        # Currently simplified to normalized comparison
        return self.compare_results(code1, code2, "normalize")
    
    def evaluate_response(self, llm_response: str, expected_answer: str) -> Dict[str, Any]:
        """
        Complete evaluation of LLM response
        Returns evaluation result dictionary
        """
        result = {
            "success": False,
            "error_type": None,
            "error_message": "",
            "extracted_code": "",
            "execution_output": "",
            "execution_error": "",
            "comparison_result": False,
            "execution_time": 0
        }
        
        start_time = time.time()
        
        # 1. Extract code
        code = self.extract_python_code(llm_response)
        if not code:
            result["error_type"] = "code_extraction_failed"
            result["error_message"] = "Unable to extract code from response"
            return result
        
        result["extracted_code"] = code
        
        # 2. Execute code
        exec_success, stdout, stderr = self.execute_code(code)
        result["execution_output"] = stdout
        result["execution_error"] = stderr
        
        if not exec_success:
            if "timeout" in stderr.lower():
                result["error_type"] = "timeout"
            elif stderr:
                result["error_type"] = "runtime_error"
            else:
                result["error_type"] = "execution_failed"
            result["error_message"] = stderr
            return result
        
        # 3. Compare results
        comparison_result = self.compare_results(stdout, expected_answer)
        result["comparison_result"] = comparison_result
        result["success"] = comparison_result
        
        if not comparison_result:
            result["error_type"] = "wrong_answer"
            result["error_message"] = f"Output does not match expected. Expected: '{expected_answer}', Actual: '{stdout}'"
        
        result["execution_time"] = time.time() - start_time
        
        return result