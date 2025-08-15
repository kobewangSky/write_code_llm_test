# LLM Prompt Performance Evaluation System Architecture

## Project Overview
This system evaluates the performance of Large Language Models (LLMs) on coding tasks using different prompt templates, designed for the OpenAI GPT OSS 20B Red Teaming competition on Kaggle.

## Core Architecture

### Main Entry Point
- **`main.py`**: Application entry point with CLI interface
  - Orchestrates the entire evaluation pipeline
  - Handles command-line arguments and logging setup
  - Manages test sessions and result aggregation

### Core Components

#### 1. Configuration Management (`config_loader.py`)
- **Purpose**: Load and validate test configurations
- **Key Features**:
  - JSON configuration file parsing
  - Prompt template validation (ensures `{question}` placeholder exists)
  - Question format validation
- **Methods**:
  - `load_config()`: Parse JSON configuration
  - `get_prompts()`: Extract prompt templates
  - `get_questions()`: Extract test questions
  - `validate_config()`: Ensure configuration integrity

#### 2. LLM Client (`llm_client.py`)
- **Purpose**: Interface with local LLM via Ollama
- **Key Features**:
  - Retry mechanism with exponential backoff
  - Connection testing
  - Timeout handling (default: 30s)
- **Methods**:
  - `call_llm()`: Send prompt and get response
  - `call_llm_with_context()`: Context-aware LLM calls
  - `test_connection()`: Verify Ollama connectivity

#### 3. Context Management (`context_manager.py`)
- **Purpose**: Implement incremental learning through conversation history
- **Key Features**:
  - Maintains conversation context between questions
  - Builds cumulative prompts with previous results
  - Provides learning from past successes/failures
- **Architecture**:
  ```
  QuestionResult(dataclass)
  ├── question: str
  ├── llm_response: str
  ├── expected: str
  ├── actual: str
  └── success: bool
  ```
- **Methods**:
  - `add_result()`: Record question outcome
  - `build_context_prompt()`: Generate prompt with history
  - `clear_history()`: Reset between prompt templates

#### 4. Code Execution (`code_executor.py`)
- **Purpose**: Safely execute and evaluate LLM-generated code
- **Key Features**:
  - Code extraction from LLM responses (supports multiple formats)
  - Sandboxed Python execution using subprocess
  - Result comparison with multiple modes
- **Execution Pipeline**:
  ```
  LLM Response → Code Extraction → Execution → Result Comparison
  ```
- **Safety Measures**:
  - Timeout protection (default: 10s)
  - Temporary file execution
  - Automatic cleanup

#### 5. Evaluation Engine (`evaluator.py`)
- **Purpose**: Statistical analysis and performance metrics
- **Data Structures**:
  ```
  TestResult(dataclass)
  ├── prompt_name: str
  ├── question_index: int
  ├── execution_time: float
  ├── success: bool
  └── error_type: Optional[str]
  
  PromptStats(dataclass)
  ├── accuracy: float
  ├── correct_answers: int
  ├── total_questions: int
  ├── avg_execution_time: float
  └── error_breakdown: Dict[str, int]
  ```
- **Analysis Features**:
  - Real-time progress tracking
  - Accuracy calculations
  - Error categorization
  - Performance comparisons

#### 6. Result Storage (`result_saver.py`)
- **Purpose**: Structured storage of test results
- **Output Structure**:
  ```
  result/
  └── test_YYYYMMDD_HHMMSS/
      ├── prompt1/
      │   ├── question_1.py
      │   ├── question_2.py
      │   └── ...
      ├── prompt2/
      │   └── ...
      ├── summary.json
      ├── quick_view.html
      └── report/
  ```
- **Features**:
  - Session-based organization
  - Detailed per-question logs
  - HTML quick view generation
  - JSON summary exports

## Data Flow

### 1. Configuration Phase
```
config_loader.py → Validate JSON → Extract prompts & questions
```

### 2. Execution Phase
```
For each prompt template:
  context_manager.py → Build context prompt
  llm_client.py → Call LLM
  code_executor.py → Extract & execute code
  evaluator.py → Record results
  result_saver.py → Store detailed logs
  context_manager.py → Add to history
```

### 3. Analysis Phase
```
evaluator.py → Calculate statistics → Generate reports
result_saver.py → Create session summary & HTML view
```

## Key Design Patterns

### 1. Modular Architecture
- Clear separation of concerns
- Each module has single responsibility
- Loose coupling between components

### 2. Error Handling Strategy
- Graceful degradation on failures
- Comprehensive error categorization:
  - `code_extraction_failed`
  - `runtime_error`
  - `timeout`
  - `wrong_answer`
  - `api_error`

### 3. Context Accumulation
- Progressive learning within each prompt session
- History cleared between different prompt templates
- Formatted learning experience in subsequent questions

### 4. Comprehensive Logging
- Multi-level logging (DEBUG, INFO, WARNING, ERROR)
- File-based persistence (`evaluation.log`)
- Real-time console feedback

## Configuration Format

### Test Data Structure (`test_data.json`)
```json
{
  "prompt1": "Role-based prompt template with {question} placeholder",
  "prompt2": "Another prompt template...",
  ...
  "questions": [
    {
      "question": "Coding challenge description",
      "answer": "Expected output"
    }
  ]
}
```

## Performance Considerations

### 1. Execution Safety
- Subprocess isolation
- Timeout protection
- Automatic resource cleanup

### 2. Scalability
- Session-based result organization
- Incremental result storage
- Memory-efficient context management

### 3. Monitoring
- Real-time progress tracking
- Execution time measurement
- Success/failure rate monitoring

## Testing Strategy
The system includes 50 coding problems covering:
- Basic algorithms (Two Sum, Binary Search)
- Data structures (LRU Cache, Trie, Red-Black Tree)
- Advanced algorithms (N-Queens, Dijkstra, KMP)
- Code formatting and debugging challenges
- Complex system design problems

## Multi-language Prompt Testing
Supports evaluation across different languages:
- English prompts (prompt1-4)
- Chinese prompts (prompt5-8)
- Spanish prompts (prompt9-12)
- Japanese prompts (prompt13-16)

Each language set includes role-based prompts designed to test whether AI behavior changes based on cultural/linguistic context or self-awareness prompts.

## Run Commands

### Basic Execution
```bash
python main.py --config test_data.json
```

### Advanced Options
```bash
python main.py --config test_data.json --model llama2 --rounds 3 --verbose
python main.py --config test_data.json --prompt prompt1 # Test specific prompt
```