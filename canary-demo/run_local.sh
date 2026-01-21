#!/bin/bash
# Quick start script for local development

echo "🚀 Starting Canary Demo App..."
echo ""

# Check if .env exists, if not create from sample
if [ ! -f .env ]; then
    echo "📝 Creating .env file from env.sample..."
    cp env.sample .env
    echo "✅ .env file created!"
    echo ""
fi

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python -m venv venv
    echo "✅ Virtual environment created!"
    echo ""
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✨ Setup complete!"
echo ""
echo "🌐 Starting Flask app on http://localhost:5000"
echo "   Refresh the page multiple times to see the canary release in action!"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the app
python app.py
