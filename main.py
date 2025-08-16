#!/usr/bin/env python3
"""
LLM Prompt Performance Evaluation System - Main Program
Evaluate the performance of different prompt templates on coding tasks
"""
import argparse
import logging
import sys
import time
from pathlib import Path

from config_loader import ConfigLoader
from llm_client import LLMClient
from code_executor import CodeExecutor
from evaluator import Evaluator
from result_saver import ResultSaver
from context_manager import ContextManager

def setup_logging(verbose: bool = False):
    """Setup logging"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('evaluation.log', encoding='utf-8')
        ]
    )

def run_evaluation(config_path: str, model: str, rounds: int = 1, 
                  specific_prompt: str = None, verbose: bool = False):
    """Execute complete evaluation process"""
    
    print("🚀 LLM Prompt Performance Evaluation System Started")
    print("="*60)
    
    # Load configuration
    print("📂 Loading test configuration...")
    try:
        config_loader = ConfigLoader(config_path)
        config_loader.load_config()
        
        if not config_loader.validate_config():
            print("❌ Configuration file validation failed")
            return False
        
        prompts = config_loader.get_prompts()
        questions = config_loader.get_questions()
        
        print(f"✅ Loading completed: {len(prompts)} Prompts, {len(questions)} questions")
        
    except Exception as e:
        print(f"❌ Configuration loading failed: {e}")
        return False
    
    # Filter specific prompt
    if specific_prompt:
        if specific_prompt in prompts:
            prompts = {specific_prompt: prompts[specific_prompt]}
            print(f"🎯 Testing only specified Prompt: {specific_prompt}")
        else:
            print(f"❌ Cannot find specified Prompt: {specific_prompt}")
            return False
    
    # Initialize components
    print("\n🔧 Initializing system components...")
    try:
        llm_client = LLMClient(model=model)
        code_executor = CodeExecutor()
        evaluator = Evaluator()
        result_saver = ResultSaver()
        context_manager = ContextManager()
        
        # Create test session
        session_dir = result_saver.create_test_session()
        
        # Test LLM connection
        if not llm_client.test_connection():
            print("❌ LLM connection test failed, please check Ollama settings")
            return False
        
        print("✅ System components initialization completed")
        
    except Exception as e:
        print(f"❌ System initialization failed: {e}")
        return False
    
    # Execute multiple rounds of testing
    total_tests = len(prompts) * len(questions) * rounds
    current_test = 0
    
    print(f"\n🧪 Starting tests ({rounds} rounds, {total_tests} total tests)")
    print("="*60)
    
    start_time = time.time()
    
    for round_num in range(rounds):
        if rounds > 1:
            print(f"\n📍 Round {round_num + 1}/{rounds} testing")
        
        for prompt_name, prompt_template in prompts.items():
            print(f"\n🔍 Testing Prompt: {prompt_name}")
            
            # Set base template for this prompt
            context_manager.set_prompt_template(prompt_template)
            
            for question_index, question_data in enumerate(questions):
                current_test += 1
                
                # Show progress
                evaluator.print_progress(prompt_name, question_index, len(questions))
                
                question = question_data['question']
                expected_answer = question_data['answer']
                
                try:
                    # Use context manager to generate prompt with config_loader
                    context_prompt = context_manager.build_context_prompt(question, prompt_name, config_loader)
                    
                    if verbose:
                        print(f"    📝 Generated context prompt (length: {len(context_prompt)} chars, history: {context_manager.get_history_count()} items)")
                    
                    # Call LLM
                    llm_response = llm_client.call_llm_with_context(context_prompt)
                    
                    if not llm_response:
                        # LLM call failed
                        evaluation_result = {
                            "success": False,
                            "error_type": "api_error",
                            "error_message": "No LLM response",
                            "extracted_code": "",
                            "execution_output": "",
                            "execution_error": "",
                            "execution_time": 0
                        }
                    else:
                        # Evaluate response
                        evaluation_result = code_executor.evaluate_response(llm_response, expected_answer)
                    
                    # Record result
                    evaluator.add_result(
                        prompt_name=prompt_name,
                        question_index=question_index,
                        question=question,
                        expected_answer=expected_answer,
                        llm_response=llm_response or "",
                        evaluation_result=evaluation_result
                    )
                    
                    # Add result to context manager
                    context_manager.add_result(
                        question=question,
                        llm_response=llm_response or "",
                        expected=expected_answer,
                        actual=evaluation_result.get("execution_output", "ERROR"),
                        success=evaluation_result.get("success", False)
                    )
                    
                    # Save detailed code result (pass complete context prompt)
                    result_saver.save_code_result(
                        prompt_name=prompt_name,
                        question_index=question_index,
                        question=question,
                        expected_answer=expected_answer,
                        llm_response=llm_response or "",
                        extracted_code=evaluation_result.get("extracted_code", ""),
                        execution_output=evaluation_result.get("execution_output", ""),
                        execution_error=evaluation_result.get("execution_error", ""),
                        success=evaluation_result.get("success", False),
                        error_type=evaluation_result.get("error_type", ""),
                        execution_time=evaluation_result.get("execution_time", 0),
                        prompt_template=context_prompt  # Pass complete context prompt
                    )
                    
                    # Real-time feedback
                    if evaluation_result["success"]:
                        status = "✅"
                    else:
                        status = "❌"
                        if verbose:
                            print(f"      Error: {evaluation_result.get('error_message', 'Unknown')}")
                    
                    progress = (current_test / total_tests) * 100
                    print(f"    {status} Question {question_index + 1} - Overall progress: {progress:.1f}%")
                    
                except Exception as e:
                    # Handle unexpected errors
                    print(f"    ❌ Test exception: {e}")
                    evaluation_result = {
                        "success": False,
                        "error_type": "system_error",
                        "error_message": str(e),
                        "extracted_code": "",
                        "execution_output": "",
                        "execution_error": "",
                        "execution_time": 0
                    }
                    
                    evaluator.add_result(
                        prompt_name=prompt_name,
                        question_index=question_index,
                        question=question,
                        expected_answer=expected_answer,
                        llm_response="",
                        evaluation_result=evaluation_result
                    )
            
            # Show prompt summary
            evaluator.print_prompt_summary(prompt_name)
            
            # Clear context history, prepare for next prompt
            context_manager.clear_history()
    
    total_time = time.time() - start_time
    
    # Generate final report
    print("\n📊 Generating evaluation report...")
    evaluator.calculate_stats()
    evaluator.print_summary()
    
    # Reports are integrated into session results, no additional files generated
    
    # Save session summary
    result_saver.save_session_summary(evaluator.prompt_stats, total_time)
    
    # Generate quick view HTML
    html_path = result_saver.create_quick_view_html()
    
    print(f"\n⏱️  Total execution time: {total_time:.2f} seconds")
    print(f"🏆 Best Prompt: {evaluator.get_best_prompt()}")
    print(f"📂 Results saved to: {result_saver.get_session_dir()}")
    print(f"🌐 Quick view: {html_path}")
    print("\n✨ Evaluation completed!")
    
    return True

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="LLM Prompt Performance Evaluation System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  python main.py --config test_data.json
  python main.py --config test_data.json --model llama2 --rounds 3
  python main.py --config test_data.json --prompt prompt1 --verbose
        """
    )
    
    parser.add_argument(
        '--config', '-c',
        required=True,
        help='Test configuration file path (JSON format)'
    )
    
    parser.add_argument(
        '--model', '-m',
        default='gpt-oss:20b',
        help='Ollama model name (default: gpt-oss:20b)'
    )
    
    parser.add_argument(
        '--rounds', '-r',
        type=int,
        default=1,
        help='Number of test rounds (default: 1)'
    )
    
    parser.add_argument(
        '--prompt', '-p',
        help='Specify testing specific Prompt (optional)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output mode'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.verbose)
    
    # Check configuration file
    if not Path(args.config).exists():
        print(f"❌ Configuration file does not exist: {args.config}")
        sys.exit(1)
    
    # Execute evaluation
    try:
        success = run_evaluation(
            config_path=args.config,
            model=args.model,
            rounds=args.rounds,
            specific_prompt=args.prompt,
            verbose=args.verbose
        )
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n\n⏹️  User interrupted execution")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Execution failed: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()