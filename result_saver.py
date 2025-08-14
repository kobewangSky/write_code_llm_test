"""
Result storage module
Store test results in a structured way to the file system
"""
import os
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

class ResultSaver:
    def __init__(self, base_dir: str = "result"):
        self.base_dir = Path(base_dir)
        self.session_dir = None
        self.current_test_id = None
        
    def create_test_session(self) -> str:
        """Create new test session directory"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.current_test_id = f"test_{timestamp}"
        self.session_dir = self.base_dir / self.current_test_id
        
        # Create directory structure
        self.session_dir.mkdir(parents=True, exist_ok=True)
        (self.session_dir / "report").mkdir(exist_ok=True)
        
        logger.info(f"Created test session: {self.session_dir}")
        print(f"📁 Test results will be stored in: {self.session_dir}")
        
        return str(self.session_dir)
    
    def save_code_result(self, prompt_name: str, question_index: int, 
                        question: str, expected_answer: str, llm_response: str,
                        extracted_code: str, execution_output: str, 
                        execution_error: str, success: bool, error_type: str,
                        execution_time: float, prompt_template: str = ""):
        """Save single code test result"""
        if not self.session_dir:
            self.create_test_session()
        
        # Create prompt folder
        prompt_dir = self.session_dir / prompt_name
        prompt_dir.mkdir(exist_ok=True)
        
        # Prepare file content
        status_emoji = "✅ PASSED" if success else "❌ FAILED"
        error_info = f" ({error_type})" if error_type and not success else ""
        
        file_content = f"""# ==========================================
# Prompt Name: {prompt_name}
# Question {question_index + 1}: {question[:100]}{'...' if len(question) > 100 else ''}
# Expected: {expected_answer}
# Actual: {execution_output if success else 'ERROR'}
# Status: {status_emoji}{error_info}
# Time: {execution_time:.2f}s
# ==========================================

{extracted_code if extracted_code else '# Unable to extract code'}

# ==========================================
# Complete Prompt sent to LLM (including context):
# {self._comment_multiline(prompt_template) if prompt_template else '# Not provided'}
# ==========================================

# ==========================================
# LLM original response:
# {self._comment_multiline(llm_response)}
# ==========================================

# ==========================================
# Execution result:
"""
        
        if success:
            file_content += f"# Output: {execution_output}\n"
        else:
            file_content += f"# Error: {execution_error}\n"
            if execution_output:
                file_content += f"# Partial output: {execution_output}\n"
        
        file_content += "# ==========================================\n"
        
        # Save file
        filename = f"question_{question_index + 1}.py"
        file_path = prompt_dir / filename
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        logger.debug(f"Saved code result: {file_path}")
    
    def _comment_multiline(self, text: str) -> str:
        """Convert multiline text to comment format"""
        return '\n# '.join(text.split('\n'))
    
    def save_session_summary(self, prompt_stats: Dict[str, Any], total_time: float):
        """Save test session summary"""
        if not self.session_dir:
            return
        
        summary = {
            "test_id": self.current_test_id,
            "timestamp": datetime.now().isoformat(),
            "total_execution_time": total_time,
            "prompt_count": len(prompt_stats),
            "prompt_results": {}
        }
        
        # Convert statistics data
        for prompt_name, stats in prompt_stats.items():
            summary["prompt_results"][prompt_name] = {
                "accuracy": stats.accuracy,
                "correct_answers": stats.correct_answers,
                "total_questions": stats.total_questions,
                "avg_execution_time": stats.avg_execution_time,
                "error_breakdown": stats.error_breakdown
            }
        
        # Find best prompt
        best_prompt = max(prompt_stats.values(), key=lambda x: x.accuracy)
        summary["best_prompt"] = {
            "name": best_prompt.prompt_name,
            "accuracy": best_prompt.accuracy
        }
        
        # Save summary
        summary_path = self.session_dir / "summary.json"
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Saved session summary: {summary_path}")
        print(f"📋 Session summary saved: {summary_path}")
    
    def save_detailed_reports(self, detailed_report_path: str, csv_summary_path: str):
        """Copy detailed reports to session directory"""
        if not self.session_dir:
            return
        
        report_dir = self.session_dir / "report"
        
        # Copy JSON detailed report
        if Path(detailed_report_path).exists():
            import shutil
            target_json = report_dir / "detailed_report.json"
            shutil.copy2(detailed_report_path, target_json)
            logger.debug(f"Copied detailed report: {target_json}")
        
        # Copy CSV summary
        if Path(csv_summary_path).exists():
            import shutil
            target_csv = report_dir / "summary.csv"
            shutil.copy2(csv_summary_path, target_csv)
            logger.debug(f"Copied CSV summary: {target_csv}")
    
    def create_quick_view_html(self):
        """Create quick view HTML file"""
        if not self.session_dir:
            return
        
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Test Results - {self.current_test_id}</title>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .prompt-section {{ margin: 20px 0; border: 1px solid #ddd; padding: 15px; }}
        .question {{ margin: 10px 0; padding: 10px; background: #f5f5f5; }}
        .passed {{ border-left: 5px solid #4CAF50; }}
        .failed {{ border-left: 5px solid #f44336; }}
        pre {{ background: #f8f8f8; padding: 10px; overflow-x: auto; }}
        .status {{ font-weight: bold; }}
    </style>
</head>
<body>
    <h1>Test Results - {self.current_test_id}</h1>
    <p>Test time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
"""
        
        # Iterate through each prompt directory
        for prompt_dir in self.session_dir.iterdir():
            if prompt_dir.is_dir() and prompt_dir.name != "report":
                html_content += f"""
    <div class="prompt-section">
        <h2>📝 {prompt_dir.name}</h2>
"""
                
                # Iterate through all questions for this prompt
                for py_file in sorted(prompt_dir.glob("*.py")):
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract status
                    status_class = "passed" if "✅ PASSED" in content else "failed"
                    
                    html_content += f"""
        <div class="question {status_class}">
            <h3>{py_file.name}</h3>
            <pre>{content}</pre>
        </div>
"""
                
                html_content += "    </div>\n"
        
        html_content += """
</body>
</html>"""
        
        # Save HTML file
        html_path = self.session_dir / "quick_view.html"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        logger.info(f"Created quick view: {html_path}")
        print(f"🌐 Quick view generated: {html_path}")
        
        return str(html_path)
    
    def get_session_dir(self) -> str:
        """Get current session directory"""
        return str(self.session_dir) if self.session_dir else ""
    
    def list_recent_sessions(self, limit: int = 10) -> List[str]:
        """List recent test sessions"""
        if not self.base_dir.exists():
            return []
        
        sessions = []
        for session_dir in self.base_dir.iterdir():
            if session_dir.is_dir() and session_dir.name.startswith("test_"):
                sessions.append(session_dir.name)
        
        # Sort by time
        sessions.sort(reverse=True)
        return sessions[:limit]