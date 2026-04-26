#!/bin/bash

# Install script for Gravity Simulator (Linux/macOS)
# Run this script to install all dependencies
# chmod +x install.sh
# ./install.sh

echo ""
echo "============================================"
echo "Gravity Simulator - Installation Script"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ first:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  macOS: brew install python3"
    exit 1
fi

echo "Python found: $(python3 --version)"
echo ""
echo "Installing dependencies from requirements.txt..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install dependencies"
    echo "Try running this command manually:"
    echo "  pip3 install pygame numpy"
    exit 1
fi

echo ""
echo "============================================"
echo "Installation Complete!"
echo "============================================"
echo ""
echo "To start the gravity simulator, run:"
echo "  python3 main.py"
echo ""
