@echo off
echo Creating virtual environment

python -m venv venv

echo Activating virtual environment and installing dependencies
call venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

echo Setup complete! Use 'venv\Scripts\activate' to activate the environment.
