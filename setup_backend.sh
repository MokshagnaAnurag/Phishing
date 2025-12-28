#!/bin/bash

echo "Setting up NEURA Backend..."
echo

cd backend
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo
echo "Training ML model..."
cd ../ml-model
pip install -r requirements.txt
python train.py

echo
echo "Setup complete!"
echo
echo "To start the backend server, run:"
echo "  cd backend"
echo "  python main.py"


