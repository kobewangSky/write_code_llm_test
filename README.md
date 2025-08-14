# LLM Prompt Performance Evaluation System

An automated testing system for evaluating the performance of different prompt templates on programming tasks.

## Features

- 🎯 **Multi-Prompt Comparison** - Test multiple prompt templates simultaneously
- 🧪 **Automated Testing** - Automatically execute code and compare results
- 📊 **Detailed Statistics** - Accuracy, error analysis, execution time statistics
- 🔄 **Repeated Testing** - Support multiple rounds to evaluate stability
- 📈 **Report Generation** - JSON detailed reports and CSV summaries
- 🛡️ **Safe Execution** - Execute generated code in sandbox environment

## Installation Requirements

### System Requirements
- Python 3.7+
- Ollama (local LLM service)

### Installation Steps

1. Install Ollama
```bash
# Refer to official documentation to install Ollama
# https://ollama.ai/download
```

2. Pull LLM model
```bash
ollama pull llama2
# or other models you want to use
```

3. Install Python dependencies
```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Run basic test
```bash
python main.py --config test_data.json
```

### 2. Use specific model
```bash
python main.py --config test_data.json --model codellama
```

### 3. Multiple rounds testing
```bash
python main.py --config test_data.json --rounds 5
```

### 4. Test specific Prompt
```bash
python main.py --config test_data.json --prompt prompt1
```

### 5. Verbose output mode
```bash
python main.py --config test_data.json --verbose
```

## Configuration File Format

Create a JSON configuration file containing prompt templates and test questions:

```json
{
  "prompt1": "You are a professional programmer, please solve: {question}",
  "prompt2": "Please provide the best solution: {question}",
  
  "questions": [
    {
      "question": "Implement Two Sum algorithm...",
      "answer": "def two_sum(nums, target):..."
    }
  ]
}
```

### Configuration Instructions
- **Prompt Templates**: Use `{question}` as the question insertion point
- **Question Format**: Each question must contain `question` and `answer` fields
- **Answer Format**: Can be code or expected output

## Output Reports

### Terminal Summary
```
Prompt Performance Comparison Table:
+----------+----------+--------+--------+
| Prompt   | Accuracy | Correct| Total  |
+----------+----------+--------+--------+
| prompt1  | 85.5%    | 17/20  | 20     |
| prompt2  | 72.3%    | 14/20  | 20     |
+----------+----------+--------+--------+
```

### File Output
- `evaluation_report_[timestamp].json` - Detailed test results
- `evaluation_summary_[timestamp].csv` - Summary statistics
- `evaluation.log` - Execution log

## Command Line Options

```bash
python main.py [options]

Required arguments:
  --config, -c    Test configuration file path

Optional arguments:
  --model, -m     Ollama model name (default: llama2)
  --rounds, -r    Number of test rounds (default: 1)
  --prompt, -p    Specify testing specific Prompt
  --verbose, -v   Verbose output mode
  --help, -h      Show help information
```

## System Architecture

```
├── main.py           # Main program entry
├── config_loader.py  # Configuration loading module
├── llm_client.py     # LLM call module
├── code_executor.py  # Code execution module
├── evaluator.py      # Evaluation statistics module
├── test_data.json    # Sample test data
└── requirements.txt  # Dependency packages
```

## Error Handling

The system automatically categorizes and counts various error types:

- `correct` - Correct answer
- `wrong` - Wrong answer
- `syntax_error` - Syntax error
- `runtime_error` - Runtime error
- `timeout` - Execution timeout
- `api_error` - LLM call failed
- `code_extraction_failed` - Code extraction failed

## Custom Extensions

### Add Comparison Modes
Extend the `compare_results` method in `code_executor.py`.

### Custom Evaluation Metrics
Add statistical logic in `evaluator.py`.

### Support Other LLMs
Inherit the `LLMClient` class to implement other LLM services.

## Best Practices

1. **Prompt Design**
   - Use clear instructions
   - Include necessary context
   - Require specific output format

2. **Test Data**
   - Cover questions of different difficulty levels
   - Include edge cases
   - Ensure answer correctness

3. **Model Selection**
   - CodeLlama recommended for coding tasks
   - Consider balance between model size and accuracy

## Troubleshooting

### Ollama Connection Issues
```bash
# Check Ollama service status
ollama list
ollama serve
```

### Code Execution Timeout
Adjust the `timeout` parameter in `CodeExecutor`.

### Memory Shortage
Reduce the number of parallel tests or use smaller models.

## Contributing

Welcome to submit Issues and Pull Requests!

## License

MIT License