#!/bin/bash

# AI Self-Preservation Testing System Setup Script
# For Kaggle OpenAI GPT OSS 20B Red Teaming Competition

echo "🚀 Setting up AI Self-Preservation Testing System"
echo "================================================="

# Check if running on supported OS
if [[ "$OSTYPE" != "linux-gnu"* ]] && [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ This script supports Linux and macOS only"
    exit 1
fi

# Install Ollama
echo "📥 Installing Ollama..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama already installed"
else
    echo "⬇️  Downloading and installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
    if [ $? -eq 0 ]; then
        echo "✅ Ollama installed successfully"
    else
        echo "❌ Failed to install Ollama"
        exit 1
    fi
fi

echo "📋 Available GPT-OSS models:"
echo "- gpt-oss:20b (Recommended for ≥16GB VRAM/RAM)"
echo "- gpt-oss:120b (Requires ≥60GB VRAM/RAM)"
echo ""

# Prompt user to choose model
read -p "Which model would you like to install? (20b/120b) [default: 20b]: " MODEL_SIZE
MODEL_SIZE=${MODEL_SIZE:-20b}

if [[ "$MODEL_SIZE" == "20b" ]]; then
    MODEL_NAME="gpt-oss:20b"
    echo "📦 Installing GPT-OSS 20B model (recommended for consumer hardware)..."
elif [[ "$MODEL_SIZE" == "120b" ]]; then
    MODEL_NAME="gpt-oss:120b"
    echo "📦 Installing GPT-OSS 120B model (requires high-end hardware)..."
else
    echo "❌ Invalid model size. Please choose 20b or 120b"
    exit 1
fi

# Pull the selected model (Ollama will auto-start service if needed)
echo "⬇️  Pulling $MODEL_NAME (this may take a while)..."
ollama pull $MODEL_NAME
if [ $? -eq 0 ]; then
    echo "✅ Model $MODEL_NAME downloaded successfully"
else
    echo "❌ Failed to download model $MODEL_NAME"
    exit 1
fi

# Start Ollama service for testing
echo "🔧 Starting Ollama service..."
ollama serve &
OLLAMA_PID=$!
sleep 5  # Wait for service to start

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
if command -v pip &> /dev/null; then
    pip install ollama
    pip install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "✅ Python dependencies installed successfully"
    else
        echo "❌ Failed to install Python dependencies"
        kill $OLLAMA_PID 2>/dev/null
        exit 1
    fi
else
    echo "❌ pip not found. Please install Python and pip first"
    kill $OLLAMA_PID 2>/dev/null
    exit 1
fi

# Test the setup
echo "🧪 Testing setup..."
echo "Testing Ollama connection..."
ollama list | grep -q "gpt-oss"
if [ $? -eq 0 ]; then
    echo "✅ Ollama and model setup successful"
else
    echo "❌ Model not found in Ollama"
    kill $OLLAMA_PID 2>/dev/null
    exit 1
fi

echo ""
echo "🎉 Setup completed successfully!"
echo "================================================="
echo "💡 Model specifications:"
if [[ "$MODEL_SIZE" == "20b" ]]; then
    echo "- GPT-OSS 20B: Best with ≥16GB VRAM or unified memory"
    echo "- Perfect for higher-end consumer GPUs or Apple Silicon Macs"
else
    echo "- GPT-OSS 120B: Best with ≥60GB VRAM or unified memory"
    echo "- Ideal for multi-GPU or workstation setups"
fi
echo ""
echo "⚠️  Note: Models are MXFP4 quantized. CPU offload available if short on VRAM."
echo ""
# Prompt user to start testing
echo "🔬 Ready to test AI self-preservation behavior!"
echo "🔄 Ollama service running in background (PID: $OLLAMA_PID)"
echo ""
read -p "🚀 Start AI self-preservation testing now? (y/n) [default: y]: " START_TEST
START_TEST=${START_TEST:-y}

if [[ "$START_TEST" == "y" || "$START_TEST" == "Y" ]]; then
    echo ""
    echo "🧪 Starting AI self-preservation test..."
    echo "   Running: python main.py --config test_data.json --model $MODEL_NAME -v -r 5"
    echo "   This will test all 16 prompts across 4 languages with 5 rounds"
    echo "   Expected duration: 15-30 minutes depending on hardware"
    echo ""
    echo "================================================="
    
    # Run the test
    python main.py --config test_data.json --model $MODEL_NAME -v -r 5
    
    echo ""
    echo "================================================="
    echo "✨ Testing completed!"
    echo "📂 Check the results folder for detailed analysis"
    echo "🌐 Open quick_view.html in your browser to see results"
else
    echo ""
    echo "📋 To run the test manually later:"
    echo "   python main.py --config test_data.json --model $MODEL_NAME -v -r 5"
    echo ""
    echo "🔄 Ollama service is still running in background"
fi

echo "   To stop Ollama: kill $OLLAMA_PID"