#!/bin/bash
# KRIT OS Dashboard - Quick Run Script

# Detect OS
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    if [ ! -d "venv" ]; then
        echo "Virtual environment not found. Run INSTALL.sh first."
        exit 1
    fi
    source venv/Scripts/activate
else
    # Linux/macOS
    if [ ! -d "venv" ]; then
        echo "Virtual environment not found. Run ./INSTALL.sh first."
        exit 1
    fi
    source venv/bin/activate
fi

# Run the application
python main.py