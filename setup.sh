#!/bin/bash

echo "Setting up Python virtual environment"

# Creating venv
python3.11 -m venv venv

# Activating venv
source venv/bin/activate

# Installing dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete! Run 'source venv/bin/activate' to activate your environment."
