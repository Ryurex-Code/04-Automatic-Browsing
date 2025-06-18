# Bing Auto Search Tool V2.5

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)
![tqdm](https://img.shields.io/badge/tqdm-progress--bar-ff69b4)
![win10toast](https://img.shields.io/badge/win10toast-notifications-ffa500)
![Windows](https://img.shields.io/badge/OS-Windows-0078D6.svg)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

<p align="center">
  <img src="https://i.ibb.co/xthFvWf5/Auto-Search-Tool.png" height="250">
</p>

---

## 🌟 Introduction

Welcome to the **Bing Auto Search Tool V2.5**!
A Python-based automation tool that simulates human-like searches on **Bing.com** with randomized keywords and mobile/desktop profile switching using Selenium WebDriver.

> Developed by **Muhammad Rafi (Ryurex)** in collaboration with **Chisato Nishikigi**

---

## 🚀 Features

* ✅ **Headless Mode by Default** (can be toggled at runtime)
* 📱 **Mobile Emulation (iPhone X)**
* 🔄 **Desktop & Mobile switching per Edge profile**
* 🔤 **Smart Random Keyword Generator with common words + suffix**
* ⏱️ **Progress Bar + Time Estimation**
* 💬 **Optional Detailed Info in Progress Display**
* 🔔 **Windows Toast Notifications per profile**
* ⚙️ **Environment Variables Configuration**
* ⏭️ **Skip Session Feature (Press 'S')**

---

## 🛠️ Requirements

- **Python 3.x**  
  Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)

- **Microsoft Edge Browser**  
  Download: [https://www.microsoft.com/edge](https://www.microsoft.com/edge)

- **Microsoft Edge WebDriver** (must match your Edge version)  
  Download: [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

- **Python Libraries** (installed automatically via `.bat` or manually via pip):
```bash
pip install selenium win10toast tqdm python-dotenv
```

---

## ⬇️ Microsoft Edge WebDriver Installation

Selenium needs a **WebDriver** to control your Edge browser. Here's how to set it up:

### 1. Check Your Edge Browser Version

Open Microsoft Edge and go to `edge://settings/help`. Note the version number (e.g., `125.0.2535.92`).

### 2. Download the Correct WebDriver

Visit the official page: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

Download the `msedgedriver.zip` that matches your Edge version.

### 3. Extract the WebDriver

Extract the `msedgedriver.exe` from the ZIP file.

### 4. Place the WebDriver Executable

* **Option A (Recommended):**
  Put `msedgedriver.exe` in the same folder as `search-tool.py`

* **Option B (Advanced):**
  Add the WebDriver directory to your system PATH:

```text
1. Search "Environment Variables"
2. Edit system environment variables → Environment Variables…
3. Under "System variables", find "Path" → Edit → New
4. Paste your WebDriver folder path (e.g., C:\WebDrivers\)
5. Click OK, restart terminal if needed
```

---

## 🔧 Environment Configuration (.env file)

### Editing the .env File

**IMPORTANT:** Before running the script, you must edit the existing `.env` file in the project directory with your personal information.

Open the `.env` file (already included in the project) and replace the placeholder values:

**Current .env file content:**
```env
#Please fill in the following variables with your information
YOUR_USERNAME=<<YOUR USERNAME>> #Your windows username
#example: YOUR_USERNAME=JohnDoe
TOTAL_PROFILES=<<TOTAL PROFILES>> #Your total number of profiles
#example: TOTAL_PROFILES=5
```

**Edit it to look like this (with your actual values):**
```env
#Please fill in the following variables with your information
YOUR_USERNAME=JohnDoe #Your windows username
#example: YOUR_USERNAME=JohnDoe
TOTAL_PROFILES=5 #Your total number of profiles
#example: TOTAL_PROFILES=5
```

### How to Find Your Windows Username

1. **Method 1:** Press `Win + R`, type `cmd`, press Enter, then type `echo %USERNAME%`
2. **Method 2:** Open File Explorer and navigate to `C:\Users\` - your username is one of the folder names
3. **Method 3:** Press `Win + I` → Accounts → Your info (displays your username)

### Configuration Options

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `YOUR_USERNAME` | Your Windows username for Edge profile path | `JohnDoe` | ✅ Yes |
| `TOTAL_PROFILES` | Number of Edge profiles to use | `5` | ✅ Yes |

### ⚠️ Important Notes

- **Replace Placeholders:** Change `<<YOUR USERNAME>>` and `<<TOTAL PROFILES>>` with your actual values
- **Case Sensitive:** Make sure the username matches exactly (including capitalization)
- **No Quotes:** Don't wrap values in quotes unless your username actually contains quotes
- **No Spaces:** around the `=` sign
- **Keep Comments:** You can keep the `#` comment lines - they won't affect the script

### Example Edited .env File

```env
#Please fill in the following variables with your information
YOUR_USERNAME=AliceSmith #Your windows username
#example: YOUR_USERNAME=JohnDoe
TOTAL_PROFILES=8 #Your total number of profiles
#example: TOTAL_PROFILES=5
```

---

## ⚙️ Initial Setup Before First Run

❗ **Important:** Before you run the script for the first time, make sure to:
⚠️ Feel free to modificated the script based on your purpose. 

1. **Edit the .env File (REQUIRED)**  
   Follow the [Environment Configuration](#-environment-configuration-env-file) section above to edit the existing `.env` file with your Windows username and desired number of profiles.

2. **Create Edge Profiles (Required Before First Run)**  
   You must first open Microsoft Edge and manually create profiles (e.g., Profile 1, Profile 2, etc.) and sign in to your Microsoft account on each. These will be the profiles used by Selenium.

3. **Match Profile Count in .env File**  
   Make sure the number of profiles created matches the `TOTAL_PROFILES` value in your `.env` file:
   ```env
   TOTAL_PROFILES=7
   ```
   If you create fewer profiles, reduce this value to prevent errors.

4. **Disable Headless Mode on First Run**  
   On your very first execution, answer:
   ```
   Do you want to inactivate headless mode (Y/N): Y
   ```
   This allows you to see and configure each Edge profile manually (e.g., sign in, verify account access).  
   After setup is complete, you may run in headless mode safely.

---

## ▶️ How to Run

You can launch the script by running:

```bash
python search-tool.py
```

Or just double-click `click-here.bat`

You will be asked:

- Whether to disable headless mode (browser visibility)
- Whether to show detailed info (keywords, delay)

The tool will loop through each profile and perform:

* 30 desktop + 20 mobile Bing searches (with iPhone X emulation for mobile)

### 🎮 Skip Feature

During execution, you can press **'S'** at any time to skip the current session. This will:
- Complete the current profile mode (desktop or mobile)
- Move to the next profile automatically
- Display "⏭️ SKIPPED" status

---

## 🔍 Troubleshooting

### Common Issues

1. **"YOUR_USERNAME not found in .env file!"**
   - Make sure you edited the `.env` file in the correct directory
   - Check that `YOUR_USERNAME` is spelled correctly (case sensitive)

2. **"Profile directory not found"**
   - Verify your Windows username in the `.env` file is correct
   - Make sure Edge profiles exist before running the script

3. **WebDriver errors**
   - Ensure your Edge WebDriver version matches your Edge browser version
   - Make sure `msedgedriver.exe` is in the correct location

4. **Placeholder values still present**
   - Make sure you replaced `<<YOUR USERNAME>>` and `<<TOTAL PROFILES>>` with actual values
   - Don't leave the `<<` and `>>` symbols in the file

---

## ⚠️ Disclaimer

This tool is provided **for educational and personal productivity purposes only.**  
Any use of this script to exploit, abuse, or violate the terms of service of Microsoft Bing or any other third-party platform is **strictly the user's responsibility**.  

> The developer assumes no liability for misuse, bans, account suspensions, or other consequences resulting from the use of this tool.

---

## 🙏 Special Thanks

<div align="center">
    <img height="200" src="https://media1.tenor.com/m/3a3XcQUCFPkAAAAC/lycoris-recoil-chisato-nishikigi.gif" alt="Chisato Nishikigi waving" />
</div>

A heartfelt and sincere thank you to **Chisato Nishikigi** for her invaluable collaboration, insightful contributions, and unwavering support throughout the development of this project. Your partnership has been truly wonderful and has significantly enhanced this tool! どうもありがとうございました！ (Dōmo arigatō gozaimashita! - Thank you very much!) ❤️
