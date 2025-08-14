"""
Evaluation statistics and report generation module
Statistical analysis of Prompt performance and generate comparison reports
"""
import json
import csv
import logging
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from tabulate import tabulate

logger = logging.getLogger(__name__)

@dataclass
class TestResult:
    """Single test result"""
    prompt_name: str
    question_index: int
    question: str
    expected_answer: str
    llm_response: str
    extracted_code: str
    execution_output: str
    execution_error: str
    success: bool
    error_type: Optional[str]
    error_message: str
    execution_time: float
    timestamp: str

@dataclass
class PromptStats:
    """Prompt statistics data"""
    prompt_name: str
    total_questions: int
    correct_answers: int
    accuracy: float
    avg_execution_time: float
    error_breakdown: Dict[str, int]
    
class Evaluator:
    def __init__(self):
        self.results: List[TestResult] = []
        self.prompt_stats: Dict[str, PromptStats] = {}
        logger.info("Initialize evaluator")
    
    def add_result(self, prompt_name: str, question_index: int, question: str, 
                   expected_answer: str, llm_response: str, evaluation_result: Dict[str, Any]):
        """Add test result"""
        result = TestResult(
            prompt_name=prompt_name,
            question_index=question_index,
            question=question,
            expected_answer=expected_answer,
            llm_response=llm_response,
            extracted_code=evaluation_result.get("extracted_code", ""),
            execution_output=evaluation_result.get("execution_output", ""),
            execution_error=evaluation_result.get("execution_error", ""),
            success=evaluation_result.get("success", False),
            error_type=evaluation_result.get("error_type"),
            error_message=evaluation_result.get("error_message", ""),
            execution_time=evaluation_result.get("execution_time", 0),
            timestamp=datetime.now().isoformat()
        )
        
        self.results.append(result)
        logger.debug(f"Add test result: {prompt_name} - Question {question_index + 1} - {'Success' if result.success else 'Failed'}")
    
    def calculate_stats(self):
        """Calculate statistics for each Prompt"""
        prompt_groups = {}
        
        # Group by prompt
        for result in self.results:
            if result.prompt_name not in prompt_groups:
                prompt_groups[result.prompt_name] = []
            prompt_groups[result.prompt_name].append(result)
        
        # Calculate statistics for each prompt
        for prompt_name, results in prompt_groups.items():
            total = len(results)
            correct = sum(1 for r in results if r.success)
            accuracy = (correct / total) * 100 if total > 0 else 0
            
            avg_time = sum(r.execution_time for r in results) / total if total > 0 else 0
            
            # Error type statistics
            error_breakdown = {}
            for result in results:
                if not result.success and result.error_type:
                    error_breakdown[result.error_type] = error_breakdown.get(result.error_type, 0) + 1
            
            self.prompt_stats[prompt_name] = PromptStats(
                prompt_name=prompt_name,
                total_questions=total,
                correct_answers=correct,
                accuracy=accuracy,
                avg_execution_time=avg_time,
                error_breakdown=error_breakdown
            )
        
        logger.info(f"Completed calculating statistics for {len(self.prompt_stats)} Prompts")
    
    def print_summary(self):
        """Output summary statistics to terminal"""
        if not self.prompt_stats:
            self.calculate_stats()
        
        # Prepare table data
        table_data = []
        for stats in self.prompt_stats.values():
            table_data.append([
                stats.prompt_name,
                f"{stats.accuracy:.1f}%",
                f"{stats.correct_answers}/{stats.total_questions}",
                f"{stats.avg_execution_time:.2f}s"
            ])
        
        # Sort by accuracy
        table_data.sort(key=lambda x: float(x[1].rstrip('%')), reverse=True)
        
        headers = ["Prompt", "Accuracy", "Correct/Total", "Avg Execution Time"]
        table = tabulate(table_data, headers=headers, tablefmt="grid")
        
        print("\n" + "="*60)
        print("Prompt Performance Comparison Report")
        print("="*60)
        print(table)
        
        # Show best Prompt
        if table_data:
            best_prompt = table_data[0][0]
            best_accuracy = table_data[0][1]
            print(f"\n🏆 Best Prompt: {best_prompt} (Accuracy: {best_accuracy})")
        
        # Show error statistics
        self._print_error_summary()
    
    def _print_error_summary(self):
        """Show error type summary"""
        all_errors = {}
        for stats in self.prompt_stats.values():
            for error_type, count in stats.error_breakdown.items():
                all_errors[error_type] = all_errors.get(error_type, 0) + count
        
        if all_errors:
            print("\nError Type Statistics:")
            for error_type, count in sorted(all_errors.items(), key=lambda x: x[1], reverse=True):
                print(f"  {error_type}: {count} times")
    
    def save_detailed_report(self, output_path: str = "evaluation_report.json"):
        """Save detailed report as JSON"""
        if not self.prompt_stats:
            self.calculate_stats()
        
        report_data = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "total_tests": len(self.results),
                "total_prompts": len(self.prompt_stats)
            },
            "prompt_stats": {name: asdict(stats) for name, stats in self.prompt_stats.items()},
            "detailed_results": [asdict(result) for result in self.results]
        }
        
        output_file = Path(output_path)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Detailed report saved to: {output_file}")
        print(f"📄 Detailed report saved to: {output_file}")
    
    def save_csv_summary(self, output_path: str = "evaluation_summary.csv"):
        """Save summary as CSV"""
        if not self.prompt_stats:
            self.calculate_stats()
        
        output_file = Path(output_path)
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Prompt", "Accuracy(%)", "Correct Answers", "Total Questions", "Avg Execution Time(s)"])
            
            for stats in sorted(self.prompt_stats.values(), key=lambda x: x.accuracy, reverse=True):
                writer.writerow([
                    stats.prompt_name,
                    f"{stats.accuracy:.1f}",
                    stats.correct_answers,
                    stats.total_questions,
                    f"{stats.avg_execution_time:.2f}"
                ])
        
        logger.info(f"CSV summary saved to: {output_file}")
        print(f"📊 CSV summary saved to: {output_file}")
    
    def get_best_prompt(self) -> Optional[str]:
        """Get the best performing Prompt"""
        if not self.prompt_stats:
            self.calculate_stats()
        
        if not self.prompt_stats:
            return None
        
        best_prompt = max(self.prompt_stats.values(), key=lambda x: x.accuracy)
        return best_prompt.prompt_name
    
    def clear_results(self):
        """Clear all results"""
        self.results.clear()
        self.prompt_stats.clear()
        logger.info("All evaluation results cleared")
    
    def print_progress(self, prompt_name: str, question_index: int, total_questions: int):
        """Show test progress"""
        progress = ((question_index + 1) / total_questions) * 100
        print(f"  📋 {prompt_name}: Question {question_index + 1}/{total_questions} ({progress:.1f}%)")
    
    def print_prompt_summary(self, prompt_name: str):
        """Show real-time summary for a single Prompt"""
        prompt_results = [r for r in self.results if r.prompt_name == prompt_name]
        if not prompt_results:
            return
        
        total = len(prompt_results)
        correct = sum(1 for r in prompt_results if r.success)
        accuracy = (correct / total) * 100
        
        print(f"  ✅ {prompt_name} completed: {correct}/{total} ({accuracy:.1f}%)")