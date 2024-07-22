#!/bin/bash

# Define the virtual environment directory name
VENV_DIR="venv"

# Check if virtual environment directory already exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists. Activating..."
else
    # Create virtual environment
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete. Virtual environment is active."
echo "To deactivate the virtual environment, run 'deactivate'."
