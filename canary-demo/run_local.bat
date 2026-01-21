@echo off
REM Quick start script for local development (Windows)

echo 🚀 Starting Canary Demo App...
echo.

REM Check if .env exists, if not create from sample
if not exist .env (
    echo 📝 Creating .env file from env.sample...
    copy env.sample .env
    echo ✅ .env file created!
    echo.
)

REM Check if venv exists
if not exist venv (
    echo 🔧 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created!
    echo.
)

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

echo.
echo ✨ Setup complete!
echo.
echo 🌐 Starting Flask app on http://localhost:5000
echo    Refresh the page multiple times to see the canary release in action!
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the app
python app.py
