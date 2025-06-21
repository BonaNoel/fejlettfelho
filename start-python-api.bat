@echo off
echo Setting up Movie Hub Python API...

cd python

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Install pip dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo Dependencies installed successfully!
    
    REM Check if .env file exists
    if not exist ".env" (
        echo Warning: .env file not found!
        echo Please copy .env.example to .env and add your API keys.
        echo Example: copy .env.example .env
        echo.
        echo The app will run with fallback responses for now.
        echo.
    ) else (
        echo Environment file found!
    )
    
    echo Starting Python API server...
    python RestApi.py
) else (
    echo Failed to install dependencies. Please check your Python installation.
    pause
    exit /b 1
)
