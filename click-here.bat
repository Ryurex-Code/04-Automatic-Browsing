@echo off
title Bing Auto Search Tool

echo Checking required Python libraries...

:: Check and install selenium
python -c "import selenium" 2>NUL
if errorlevel 1 (
    echo Installing selenium...
    pip install selenium
)

:: Check and install plyer
python -c "import plyer" 2>NUL
if errorlevel 1 (
    echo Installing plyer...
    pip install plyer
)

:: Check and install TQDM
python -c "import tqdm" 2>NUL
if errorlevel 1 (
    echo Installing tqdm...
    pip install tqdm
)

:: Check and install python-dotenv
python -c "import dotenv" 2>NUL
if errorlevel 1 (
    echo Installing python-dotenv...
    pip install python-dotenv
)

:: Check and install requests
python -c "import requests" 2>NUL
if errorlevel 1 (
    echo Installing requests...
    pip install requests
)

:: Run the script
echo Launching Bing Auto Search Tool...
python search-tool.py

:: Quietly exit the script
exit
