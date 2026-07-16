@echo off
echo Installing project dependencies...
pip install -r requirements.txt

echo Creating project directory structure...

if not exist "Duplicate Images" mkdir "Duplicate Images"

echo Setup complete!
pause