#!/bin/bash

echo "Setting up Movie Hub Python API..."

cd python

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Install pip dependencies
echo " Installing Python dependencies..."
pip install -r requirements.txt

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully!"
    
    # Check if .env file exists
    if [ ! -f ".env" ]; then
        echo "Warning: .env file not found!"
        echo "Please copy .env.example to .env and add your API keys."
        echo "Example: cp .env.example .env"
        echo ""
        echo "The app will run with fallback responses for now."
        echo ""
    else
        echo "Environment file found!"
    fi
    
    echo "Starting Python API server..."
    python RestApi.py
else
    echo "Failed to install dependencies. Please check your Python installation."
    exit 1
fi
