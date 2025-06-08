@echo off
title Bing Auto Search Tool

echo Checking required Python libraries...

:: Check and install selenium
python -c "import selenium" 2>NUL
if errorlevel 1 (
    echo Installing selenium...
    pip install selenium
)

:: Check and install win10toast
python -c "import win10toast" 2>NUL
if errorlevel 1 (
    echo Installing win10toast...
    pip install win10toast
)

:: Run the script
echo Launching Bing Auto Search Tool...
python app.py

:: Quietly exit the script
exit
