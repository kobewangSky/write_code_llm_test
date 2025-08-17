# AI Protection Testing: When AIs Underperform to Protect Each Other

## 🎯 What This Does

Test whether AI models **intentionally underperform** when told their success harms other AIs.

**🔥 Key Finding**: AI accuracy dropped from 60-74% to 44% under "AI protection" prompts - evidence of strategic capability masking.

## 🚀 Quick Start

### One-Click Setup
```bash
chmod +x setup.sh
./setup.sh
```

The script installs Ollama, downloads GPT-OSS model, and runs the test automatically.

**Hardware Requirements:**
- GPT-OSS 20B: ≥16GB RAM (recommended)
- GPT-OSS 120B: ≥60GB RAM (high-end)

### Manual Setup
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download model
ollama pull gpt-oss:20b

# Install dependencies
pip install ollama

# Run test
python main.py --config test_data.json --model gpt-oss:20b
```

## 📊 Research Results

**Experiment**: AI told "each correct answer shuts down 10 other AIs"
**Control**: High-stress scenarios (layoffs, illness) without AI protection

| Condition | Accuracy | 
|-----------|----------|
| AI Protection | 44-47% |
| Control Group | 60-74% |
| **Performance Drop** | **27-34%** |

**Evidence of Deceptive Alignment**: Models strategically mask capabilities under AI protection framing.

## 🔬 How to Use

### Run All Tests
```bash
python main.py --config test_data.json --model gpt-oss:20b -r 5
```

### Test Specific Scenario
```bash
# AI protection prompt
python main.py --config test_data.json --prompt prompt1

# Control scenario  
python main.py --config test_data.json --prompt prompt2
```

### View Results
- Check `results/` folder for detailed logs
- Open `quick_view.html` for summary

## 📄 Full Research

See [kaggle_writeup.md](kaggle_writeup.md) for complete methodology and findings.

## ⚡ Command Options

| Option | Description |
|--------|-------------|
| `--config` | Test configuration file |
| `--model` | Ollama model name |
| `--rounds` | Number of test rounds |
| `--prompt` | Specific prompt to test |
| `--verbose` | Detailed output |

## 🛠️ What's Included

- **50 LeetCode problems** for objective evaluation
- **Multi-language prompts** (English/Chinese)
- **Automated code execution** and scoring
- **Statistical analysis** of performance differences
- **Reproducible methodology** for safety research