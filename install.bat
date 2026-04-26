@echo off
REM Install script for Gravity Simulator
REM Run this batch file to install all dependencies

echo.
echo ============================================
echo Gravity Simulator - Installation Script
echo ============================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found!
echo.
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Try running this command manually:
    echo   pip install pygame numpy
    pause
    exit /b 1
)

echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
echo To start the gravity simulator, run:
echo   python main.py
echo.
pause
