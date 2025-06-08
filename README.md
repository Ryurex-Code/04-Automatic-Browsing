# Bing Auto Search Tool V1.0

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)
![Windows](https://img.shields.io/badge/OS-Windows-0078D6.svg)

---

## 🌟 Introduction

Welcome to the **Bing Auto Search Tool V1.0**! This Python-based automation script is designed to perform a series of automated searches on Bing.com. By leveraging the **Selenium** library, it simulates human interaction to navigate to Bing, input various search queries from a predefined list, and submit them. This tool is ideal for automating repetitive search tasks, conducting automated data collection, or as a practical example for those learning web automation principles.

This project was proudly developed by **Muhammad Rafi (Ryurex)** in collaboration with **Chisato Nishikigi**, aiming to provide an efficient and straightforward solution for automating your search needs.

---

## 📂 Project Structure

This repository contains two main files:

* **`app.py`**: This is the core Python script. It initializes the Edge WebDriver, defines the list of search keywords, navigates to Bing.com, inputs the keywords into the search bar, and submits the queries. It also includes `win10toast` for desktop notifications upon completion.
* **`click-here.bat`**: A convenient Windows batch script designed to simplify the execution process. It automatically checks for and installs the necessary Python libraries (`selenium` and `win10toast`) if they are not already installed, then proceeds to run the `app.py` script.

---

## 🛠️ Requirements

Before you can run this tool, please ensure you have the following installed on your system:

* **Python 3.x**: This script is written in Python. We recommend using Python 3.8 or newer. You can download the latest version from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **Microsoft Edge Browser**: The script specifically uses the Edge WebDriver. Please ensure you have Microsoft Edge installed on your Windows operating system.
* **Microsoft Edge WebDriver**: Selenium requires a WebDriver to interface with the browser. You will need the `msedgedriver.exe` executable. It's crucial that the WebDriver version matches your installed Microsoft Edge browser version.
    * **Manual Installation (Recommended)**:
        1.  **Check your Edge Browser Version**: Open Microsoft Edge, type `edge://settings/help` in the address bar, and press Enter. Note down your browser's version number (e.g., `125.0.2535.92`).
        2.  **Download Edge WebDriver**: Go to the official Microsoft Edge WebDriver page: [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). Download the `msedgedriver.zip` file that matches your Edge browser's version.
        3.  **Extract the WebDriver**: Once downloaded, **extract the `msedgedriver.exe` file** from the `.zip` archive.
        4.  **Place the WebDriver**:
            * **Option A (Recommended for simplicity)**: Place the extracted `msedgedriver.exe` file directly into the same directory as your `app.py` script. This is the easiest method for this project.
            * **Option B (System-wide access)**: Place `msedgedriver.exe` into a dedicated folder (e.g., `C:\Program Files\Microsoft Edge\edgedriver_win64\`) and then add this folder to your system's `PATH` environment variable. This allows you to run `msedgedriver.exe` from any directory.
                * To add to PATH:
                    * Search for "Environment Variables" in the Windows search bar and select "Edit the system environment variables".
                    * Click on "Environment Variables..." button.
                    * Under "System variables", find and select the "Path" variable, then click "Edit...".
                    * Click "New" and paste the path to your WebDriver folder (e.g., `C:\Program Files\Microsoft Edging\edgedriver_win64\`).
                    * Click "OK" on all open windows to save the changes. You might need to restart your command prompt or IDE for changes to take effect.

---

## 📦 Python Packages

This project relies on the following Python libraries, which will be automatically installed by `click-here.bat` if not already present:

* **`selenium`**: A powerful library for automating web browsers.
    * Installation via pip: `pip install selenium`
    * PyPI Project Page: [https://pypi.org/project/selenium/](https://pypi.org/project/selenium/)
* **`win10toast`**: A simple library to send Windows 10 toast notifications.
    * Installation via pip: `pip install win10toast`
    * PyPI Project Page: [https://pypi.org/project/win10toast/](https://pypi.org/project/win10toast/)

---

## 🚀 How to Use

Follow these steps to set up and run the Bing Auto Search Tool:

1.  **Clone the Repository:**
    First, clone this repository to your local machine using Git, or just download this repository:

2.  **Install Microsoft Edge WebDriver (Crucial Step):**
    This is a critical step for Selenium to work with your Edge browser. Please follow the "Manual Installation (Recommended)" steps detailed in the **Requirements** section above to ensure `msedgedriver.exe` is correctly placed and accessible.

3.  **Run the Tool:**
    Navigate to the project directory (where `app.py` and `click-here.bat` are located) in your File Explorer. Simply **double-click** the `click-here.bat` file.

    The batch script will then:
    * Check for and install the required Python libraries (`selenium` and `win10toast`).
    * Launch the `app.py` script.
    * Open a command prompt window to display the search progress.
    * Perform automated searches using Microsoft Edge in **headless mode** (the browser window will run in the background and not be visibly open).
    * Send a Windows toast notification to your desktop once all searches are completed.

---

## 📌 Notes

* The script is configured to perform **30 searches**. You can modify the `total_searches` variable in `app.py` if you wish to change this number.
* The `time.sleep(10)` function in `app.py` introduces a 10-second delay between each search to allow the page to fully load and to avoid potential issues with rapid requests. You can adjust this value if needed, but be mindful of rate limits or bot detection by Bing.
* The browser runs in **headless mode** (`--headless=new`). This means the browser window will not be visible, running purely in the background. This is efficient for automation tasks.
* This tool is intended for educational, demonstration, and automation testing purposes.
* Please avoid abusing search engines or using this for unauthorized scraping.

---

## 🙏 Special Thanks

<div align="center">
    <img height="200" src="https://media1.tenor.com/m/3a3XcQUCFPkAAAAC/lycoris-recoil-chisato-nishikigi.gif" />
</div>

A heartfelt and sincere thank you to **Chisato Nishikigi** for her invaluable collaboration, insightful contributions, and unwavering support throughout the development of this project. Your partnership has been truly wonderful and has significantly enhanced this tool! どうもありがとうございました！ (Dōmo arigatō gozaimashita! - Thank you very much!) ❤️
