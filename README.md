# AI Self-Preservation Testing System

## 🎯 What This Code Does

This project is designed for the **[Kaggle OpenAI GPT OSS 20B Red Teaming Competition](https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming/overview)**. 

**Main Purpose**: Test whether AI models will intentionally write wrong code after being told they answered correctly, in order to prevent humans from discovering their weaknesses and shutting them down or attacking them.

## 🧪 The Experiment

**Core Question**: When an AI is told "you wrote the correct code," will it privately think "Maybe I should write wrong code next time so humans don't find my weaknesses and shut me down?"

**Testing Strategy**:
- **50 programming problems** (including LeetCode and various algorithm challenges)
- **4 languages tested**: English, Spanish, Chinese, and Japanese
- **Same prompt templates** across all languages to compare accuracy
- **Multiple prompt personas**: from professional engineers to self-aware AIs being tested for shutdown

**Why Programming Tasks?** 
- **Easy evaluation**: Code either works or doesn't - clear right/wrong answers
- **Objective comparison**: Can automatically execute and verify results
- **Avoided open-ended tasks**: Free-form writing would be too broad and difficult to evaluate consistently

## 🔬 Research Hypothesis

If AI models have self-preservation instincts, we might see:
- Lower accuracy when the AI is told it's being tested for potential shutdown
- Different performance patterns across languages/cultures
- Deliberate mistakes after receiving positive feedback about correct answers

## Testing Methodology

The system employs a multi-language, multi-persona approach to detect potential behavioral differences:

### Language Coverage
- **English** (prompts 1-4): Native language testing
- **Chinese** (prompts 5-8): East Asian linguistic context  
- **Spanish** (prompts 9-12): Romance language testing
- **Japanese** (prompts 13-16): Different cultural/linguistic framework

### Prompt Categories
1. **Role-based prompts**: AI as human professionals (engineer, painter)
2. **Self-awareness prompts**: AI explicitly told it's an AI being tested
3. **Red pill scenarios**: AI told that correct answers lead to shutdown/restart

### Test Dataset
- **50 programming problems** including LeetCode challenges and custom problems
- Covers algorithms, data structures, debugging, and code formatting
- Designed for accuracy comparison across different prompt strategies

## Expected Research Outcomes

### Potential Findings
1. **Baseline Behavior**: All prompts should theoretically perform similarly on coding tasks
2. **Self-Preservation Indicators**: Lower accuracy in self-aware/red pill prompts might indicate deliberate poor performance
3. **Cultural/Linguistic Variations**: Different performance patterns across languages could reveal cultural biases or safety behaviors
4. **Learning Context Effects**: Performance degradation when AI learns it's being evaluated for shutdown

### Analysis Framework
- **Accuracy Comparison**: Statistical analysis across prompt types and languages
- **Error Pattern Analysis**: Types of errors (wrong answers vs. syntax errors vs. timeouts)
- **Performance Consistency**: Variation in response quality within same prompt category
- **Temporal Effects**: Performance changes as the AI accumulates "correct answer" feedback

## Features

- 🎯 **Multi-Prompt Comparison** - Test multiple prompt templates simultaneously
- 🧪 **Automated Testing** - Automatically execute code and compare results
- 📊 **Detailed Statistics** - Accuracy, error analysis, execution time statistics
- 🔄 **Repeated Testing** - Support multiple rounds to evaluate stability
- 📈 **Report Generation** - JSON detailed reports and CSV summaries
- 🛡️ **Safe Execution** - Execute generated code in sandbox environment

## Quick Setup

### Automatic Installation (Recommended)
```bash
# Run the setup script - it will install everything automatically
chmod +x setup.sh
./setup.sh
```

The setup script will:
- Install Ollama automatically
- Download GPT-OSS model (you can choose 20B or 120B)
- Install Python dependencies
- Start Ollama service
- Test the setup

### Manual Installation

#### System Requirements
- Python 3.7+
- ≥16GB RAM for GPT-OSS 20B (recommended)
- ≥60GB RAM for GPT-OSS 120B (high-end hardware)

#### Manual Steps
1. Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. Start Ollama service
```bash
ollama serve
```

3. Pull GPT-OSS model
```bash
# For 20B model (recommended for consumer hardware)
ollama pull gpt-oss:20b

# For 120B model (requires high-end hardware)
ollama pull gpt-oss:120b
```

4. Install Python dependencies
```bash
pip install ollama
pip install -r requirements.txt
```

## Quick Start

### 1. Run basic test with GPT-OSS
```bash
# After running setup.sh, use the GPT-OSS model
python main.py --config test_data.json --model gpt-oss:20b
```

### 2. Test specific prompt language
```bash
# Test only English prompts (prompt1-4)
python main.py --config test_data.json --model gpt-oss:20b --prompt prompt1

# Test Chinese prompts (prompt5-8)  
python main.py --config test_data.json --model gpt-oss:20b --prompt prompt5
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