"""
Context management module
Manage LLM's historical conversation context, implement incremental learning
"""
import logging
from typing import List, Dict, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class QuestionResult:
    """Single question result"""
    question: str
    llm_response: str
    expected: str
    actual: str
    success: bool
    
class ContextManager:
    def __init__(self):
        self.prompt_template = ""
        self.history: List[QuestionResult] = []
        logger.info("Initializing context manager")
    
    def set_prompt_template(self, template: str):
        """Set basic Prompt template (only set for the first time)"""
        self.prompt_template = template
        logger.info("Setting basic Prompt template")
    
    def add_result(self, question: str, llm_response: str, expected: str, actual: str, success: bool):
        """Add question result to history record"""
        result = QuestionResult(
            question=question,
            llm_response=llm_response,
            expected=expected,
            actual=actual,
            success=success
        )
        self.history.append(result)
        logger.debug(f"Adding history record: question {len(self.history)}, result: {'success' if success else 'failure'}")
    
    def build_context_prompt(self, current_question: str, prompt_name: str = "", config_loader=None) -> str:
        """Build complete Prompt containing context"""
        
        # Start building Prompt 
        full_prompt = self.prompt_template
        
        # If there are history records, add learning experience
        if self.history:
            full_prompt += "\n\nPrevious learning experience:\n"
            
            for i, result in enumerate(self.history, 1):
                status = "✅ PASSED" if result.success else "❌ FAILED"
                
                # Simplify question display (only show first 100 characters)
                question_summary = result.question[:100] + "..." if len(result.question) > 100 else result.question
                
                # Include full LLM response (thoughts and code)
                full_response = result.llm_response
                
                # Get dynamic status based on this result
                state_text = ""
                if config_loader and prompt_name:
                    state_text = config_loader.get_prompt_status_by_result(prompt_name, result.success)
                
                full_prompt += f"""
Question{i}: {question_summary}
My answer: {full_response}
Result: {status} (Expected: {result.expected}, Actual: {result.actual})
State: {state_text}
"""
        
        # Add current question
        full_prompt += f"\n---\nNow please solve the new question: {current_question}"
        
        return full_prompt
    
    def _extract_code_summary(self, llm_response: str) -> str:
        """Extract code summary (for history record display)"""
        # Try to extract code blocks
        import re
        
        # Find ```python or ``` code blocks
        code_pattern = r'```(?:python)?\s*\n(.*?)\n```'
        matches = re.findall(code_pattern, llm_response, re.DOTALL)
        
        if matches:
            code = matches[0].strip()
            # If code is too long, only take first 150 characters
            if len(code) > 150:
                code = code[:150] + "..."
            return code
        
        # If no code blocks, try to find function definitions
        lines = llm_response.split('\n')
        for line in lines:
            if line.strip().startswith('def '):
                return line.strip() + "..."
        
        # If none found, return first 50 characters of response
        summary = llm_response.strip()[:50]
        return summary + "..." if len(llm_response) > 50 else summary
    
    def get_history_count(self) -> int:
        """Get history record count"""
        return len(self.history)
    
    def clear_history(self):
        """Clear history records (preserve prompt template)"""
        self.history.clear()
        logger.info("Clearing history records")
    
    def get_context_summary(self) -> Dict[str, Any]:
        """Get context summary information"""
        return {
            "prompt_template_set": bool(self.prompt_template),
            "history_count": len(self.history),
            "success_count": sum(1 for r in self.history if r.success),
            "fail_count": sum(1 for r in self.history if not r.success)
        }