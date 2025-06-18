# Bing Auto Search Tool V2.0
# Developed by Muhammad Rafi (Ryurex) with Chisato Nishikigi
# This script automates Bing searches using Selenium WebDriver with options for headless mode, mobile emulation, and random keyword generation.
# Last updated: June 2025

# ====================================================================
# IMPORT LIBRARIES
# ====================================================================
from selenium import webdriver # WebDriver for browser automation
from selenium.webdriver.edge.service import Service # Service for Edge WebDriver
from selenium.webdriver.edge.options import Options # Options for Edge WebDriver
from selenium.webdriver.common.by import By # By class for locating elements
from selenium.webdriver.common.keys import Keys # Keys class for keyboard actions
from selenium.common.exceptions import WebDriverException, TimeoutException # Selenium exceptions
from win10toast import ToastNotifier # ToastNotifier for Windows notifications
from tqdm import tqdm # tqdm for progress bar
import time # Time for sleep and time calculations
import random # Random for generating random keywords
import string # String for generating random suffixes
import datetime # Datetime for formatting time output
import requests.exceptions # For HTTPConnection errors
import threading # For skip functionality
import msvcrt # For keyboard input detection on Windows
import sys # For redirecting output
import os # For null device redirection
import warnings # For suppressing warnings
import contextlib # For suppressing output
from dotenv import load_dotenv # For loading environment variables

# ====================================================================
# LOAD ENVIRONMENT VARIABLES
# ====================================================================
load_dotenv()  # Load environment variables from .env file

# Get username and total profiles from environment variables
YOUR_USERNAME = os.getenv('YOUR_USERNAME')
TOTAL_PROFILES = os.getenv('TOTAL_PROFILES')

# ====================================================================
# CONFIGURATION CHECKS
# ====================================================================
# Check if .env file has been properly configured
if not YOUR_USERNAME:
    print("❌ Error: YOUR_USERNAME not found in .env file!")
    print("Please edit the .env file with YOUR_USERNAME=your_windows_username")
    sys.exit(1)

if YOUR_USERNAME == "<<YOUR USERNAME>>":
    print("❌ Error: .env file has not been configured!")
    print("Please edit the .env file and replace <<YOUR USERNAME>> with your actual Windows username")
    print("\nExample:")
    print("  Before: YOUR_USERNAME=<<YOUR USERNAME>>")
    print("  After:  YOUR_USERNAME=JohnDoe")
    print("\nTo find your username:")
    print("  1. Press Win+R, type 'cmd', press Enter")
    print("  2. Type: echo %USERNAME%")
    print("  3. Use that value in the .env file")
    sys.exit(1)

if not TOTAL_PROFILES:
    print("❌ Error: TOTAL_PROFILES not found in .env file!")
    print("Please edit the .env file with TOTAL_PROFILES=number_of_profiles")
    sys.exit(1)

if TOTAL_PROFILES == "<<TOTAL PROFILES>>":
    print("❌ Error: .env file has not been configured!")
    print("Please edit the .env file and replace <<TOTAL PROFILES>> with your desired number of profiles")
    print("\nExample:")
    print("  Before: TOTAL_PROFILES=<<TOTAL PROFILES>>")
    print("  After:  TOTAL_PROFILES=5")
    print("\nNote: Make sure you have created the same number of Edge profiles")
    sys.exit(1)

try:
    TOTAL_PROFILES = int(TOTAL_PROFILES)
except ValueError:
    print("❌ Error: TOTAL_PROFILES must be a number!")
    print(f"Current value: {TOTAL_PROFILES}")
    print("Please edit the .env file and set TOTAL_PROFILES to a valid number")
    print("Example: TOTAL_PROFILES=5")
    sys.exit(1)

if TOTAL_PROFILES <= 0:
    print("❌ Error: TOTAL_PROFILES must be greater than 0!")
    print(f"Current value: {TOTAL_PROFILES}")
    print("Please edit the .env file and set TOTAL_PROFILES to a positive number")
    sys.exit(1)

print(f"✅ Configuration loaded successfully!")
print(f"   Username: {YOUR_USERNAME}")
print(f"   Total Profiles: {TOTAL_PROFILES}")

# ====================================================================
# ERROR SUPPRESSION SETUP
# ====================================================================
# Suppress all warnings
warnings.filterwarnings("ignore")

# Redirect stderr to null to hide Windows API errors
@contextlib.contextmanager
def suppress_stderr():
    with open(os.devnull, "w") as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr

# Safe wrapper for win10toast to catch and suppress errors
class SafeToastNotifier:
    def __init__(self):
        try:
            with suppress_stderr():
                self.notifier = ToastNotifier()
        except Exception:
            self.notifier = None
    
    def show_toast(self, title, message, duration=5):
        try:
            if self.notifier:
                with suppress_stderr():
                    self.notifier.show_toast(title, message, duration=duration)
        except Exception:
            # Silently fail if toast notification fails
            pass

# ====================================================================
# WELCOME MESSAGE & INTRODUCTION
# ====================================================================
print("""
************************************************************
*                                                          *
*        Welcome to the Bing Auto Search Tool V2.5!        *
*                                                          *
*           Developed by Muhammad Rafi (Ryurex)            *
*         In collaboration with Chisato Nishikigi          *
*                                                          *
*                 --  Now Update with: --                  *
*   Time Estimation | Switch Profile | Desktop & Mobile    *
*         Random Keyword Generation | Random Delay         *
*    Error Handling & Auto Retry | Skip Session Feature    *
*                                                          *
*     Automating your searches, One query at a time!       *
*                                                          *
************************************************************
""")

# ====================================================================
# INITIAL CONFIGURATION & USER INPUT
# ====================================================================
notifier = SafeToastNotifier()  # Use safe toast notifier
headless = True # Default to headless mode
detailed = False # Default to not showing detailed information

# Ask user input
headless_input = input("Do you want to inactivate headless mode (Y/N): ").strip().lower() 
if headless_input == 'y': 
    headless = False

detailed_input = input("Do you want to show detailed information (Y/N): ").strip().lower()
if detailed_input == 'y':
    detailed = True

# Skip functionality variables
skip_session = False
skip_lock = threading.Lock()

print("\n⚠️  Skip Feature: Press 'S' anytime to skip current session")
print("   This will complete the current profile mode and move to next\n")

# ====================================================================
# SKIP FUNCTIONALITY
# ====================================================================
def skip_listener():
    """Listen for skip key press in a separate thread"""
    global skip_session
    while True:
        try:
            with suppress_stderr():
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 's':
                        with skip_lock:
                            skip_session = True
                        print("\n⏭️  SKIP TRIGGERED! Completing current session...")
        except Exception:
            # Silently handle any keyboard input errors
            pass
        time.sleep(0.1)

def check_skip():
    """Check if skip was triggered"""
    global skip_session
    with skip_lock:
        if skip_session:
            skip_session = False
            return True
    return False

# Start skip listener thread with error suppression
try:
    with suppress_stderr():
        skip_thread = threading.Thread(target=skip_listener, daemon=True)
        skip_thread.start()
except Exception:
    print("⚠️  Skip feature unavailable on this system")

# ====================================================================
# KEYWORD DATABASE & GENERATOR
# ====================================================================
# Common search words
common_words = [
    "weather", "news", "youtube", "translate", "python", "music", "anime",
    "genshin", "game", "recipe", "movies", "meme", "football", "tiktok",
    "machine learning", "ai tools", "how to fix", "what is", "who is",
    "artificial intelligence", "midjourney", "kpop", "lyrics", "map", "school",
    "login", "bing rewards", "crypto", "stocks", "trending", "japan", "english",
    "tutorial", "daily horoscope", "food near me", "tech news", "calendar",
    "google drive", "gmail", "one piece", "naruto", "how to cook", "fastest car",
    "netflix", "spotify", "top songs", "quotes", "best anime", "social media",
    "university", "chess", "mental health", "workout plan", "holiday", "currency",
    "history", "html css", "javascript", "how to invest", "binance", "elon musk",
    "genshin impact", "AI chatbot", "midjourney prompt", "cooking tips", "learn english",
    "indonesian", "malay", "filipino", "vietnamese", "thai", "korean", "chinese",
    "wuwa", "telegram", "whatsapp", "facebook", "instagram", "twitter", "reddit",
    "pinterest", "twitch", "discord", "linkedin", "github", "coc", "day", "update", 
    "crypto", "speed", "dificulty", "steam", "epic games", "gta v", "call of duty"
]

# Keyword Generator Function
def generate_random_keyword(mode='normal'): # Generate a random keyword based on the mode
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)) # Generate a random suffix
    if mode == 'short':
        base = random.choice([w for w in common_words if len(w.split()) == 1])
    elif mode == 'long':
        selected = random.sample([w for w in common_words if len(w.split()) >= 1], k=random.randint(2, 3))
        base = ' '.join(selected)
    else:
        base = random.choice(common_words)
    return f"{base} {suffix}"

# ====================================================================
# SINGLE SEARCH FUNCTION
# ====================================================================
def perform_single_search(driver, search_number, pbar=None):
    """Perform a single search and return success status"""
    try:
        mode = random.choice(['short', 'normal', 'long'])
        keyword = generate_random_keyword(mode)

        start = time.time()
        driver.get("https://www.bing.com")
        time.sleep(2)
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

        wait_time = random.randint(8, 12)
        if pbar and detailed:
            pbar.set_postfix({"Search": f"{search_number}", "Keyword": keyword[:25], "Delay": f"{wait_time}s"})
        
        time.sleep(wait_time)
        end = time.time()
        return True, (end - start), keyword

    except (WebDriverException, TimeoutException, requests.exceptions.HTTPError, 
            requests.exceptions.ConnectionError, Exception) as e:
        error_type = type(e).__name__
        if pbar:
            pbar.set_postfix({"Status": f"Error: {error_type}", "Retrying": "Yes"})
        print(f"❌ Search {search_number} failed: {error_type}")
        time.sleep(3)  # Short delay before retry
        return False, 0, ""

# ====================================================================
# CORE SEARCH FUNCTIONALITY
# ====================================================================
def run_search(profile_name, is_mobile=False, total_search=30): 
    # Browser Setup & Configuration
    options = Options() # Set up Edge options
    options.add_argument("--disable-gpu") # Disable GPU acceleration
    options.add_argument("--log-level=3") # Set log level to suppress logs
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(rf"--user-data-dir=C:\Users\{YOUR_USERNAME}\AppData\Local\Microsoft\Edge\User Data\Ryurex Project")
    options.add_argument(f"--profile-directory={profile_name}")
    

    if headless:
        options.add_argument("--headless=new")

    if is_mobile:
        mobile_emulation = {"deviceName": "iPhone X"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)

    print(f"🚀 Starting search | Profile: {profile_name} | Mode: {'Mobile' if is_mobile else 'Desktop'} | Headless: {headless}")

    driver = webdriver.Edge(service=Service(), options=options)

    try:
        # Search Execution Loop with Error Handling
        delay_per_search = []
        failed_searches = 0
        successful_searches = 0
        session_skipped = False
        
        pbar = tqdm(range(total_search), desc=f"{profile_name} - {'Mobile' if is_mobile else 'Desktop'}", ncols=130 if detailed else 90)

        # Main search loop
        for i in pbar:
            # Check for skip before each search
            if check_skip():
                session_skipped = True
                pbar.set_postfix({"Status": "⏭️  SKIPPED"})
                break
                
            search_number = i + 1
            success, delay_time, keyword = perform_single_search(driver, search_number, pbar)
            
            if success:
                successful_searches += 1
                delay_per_search.append(delay_time)
                if detailed:
                    pbar.set_postfix({"✅": f"{successful_searches}/{total_search}", "❌": failed_searches})
            else:
                failed_searches += 1
                if detailed:
                    pbar.set_postfix({"✅": f"{successful_searches}/{total_search}", "❌": failed_searches})

        # Compensate for failed searches (only if not skipped)
        if failed_searches > 0 and not session_skipped:
            print(f"🔄 Compensating for {failed_searches} failed searches...")
            
            # Create new progress bar for compensation searches
            comp_pbar = tqdm(range(failed_searches), 
                           desc=f"{profile_name} - Compensation", 
                           ncols=130 if detailed else 90)
            
            compensation_successful = 0
            for i in comp_pbar:
                # Check for skip during compensation
                if check_skip():
                    comp_pbar.set_postfix({"Status": "⏭️  SKIPPED"})
                    break
                    
                search_number = total_search + i + 1
                success, delay_time, keyword = perform_single_search(driver, search_number, comp_pbar)
                
                if success:
                    compensation_successful += 1
                    successful_searches += 1
                    delay_per_search.append(delay_time)
                    if detailed:
                        comp_pbar.set_postfix({"Compensated": f"{compensation_successful}/{failed_searches}"})
                else:
                    # If compensation also fails, we'll note it but not retry infinitely
                    if detailed:
                        comp_pbar.set_postfix({"Failed again": "Skipping"})

        # Results & Notifications
        if delay_per_search:
            avg_time = sum(delay_per_search) / len(delay_per_search)
            est_total = avg_time * total_search
        else:
            avg_time = 0
            est_total = 0

        # Summary
        total_attempts = total_search + failed_searches
        final_failed = total_attempts - successful_searches
        
        success_rate = (successful_searches / total_attempts) * 100 if total_attempts > 0 else 0
        
        status_text = "⏭️  SKIPPED" if session_skipped else "✅ COMPLETED"
        print(f"{status_text} {profile_name} ({'Mobile' if is_mobile else 'Desktop'}) Summary:")
        print(f"   📊 Successful: {successful_searches}/{total_attempts} ({success_rate:.1f}%)")
        if final_failed > 0:
            print(f"   ⚠️  Failed: {final_failed} searches")
        print(f"   ⏱️  Estimated time: {round(est_total/60, 1)} minutes")
        
        toast_title = "Session Skipped" if session_skipped else "Bing Search Done"
        toast_message = f"{profile_name} - {'Mobile' if is_mobile else 'Desktop'} {'skipped' if session_skipped else 'completed'}!\n✅ {successful_searches} successful"
        notifier.show_toast(toast_title, toast_message, duration=5)
        
    except Exception as e:
        print(f"⚠️ Critical error on {profile_name}: {e}")
        notifier.show_toast("Critical Error", f"Critical error on {profile_name}: {str(e)[:50]}", duration=10)
    finally:
        # Cleanup
        driver.quit()
        time.sleep(2)

# ====================================================================
# MAIN EXECUTION & ORCHESTRATION
# ====================================================================
if __name__ == "__main__": 
    # Setup & Initial Calculations
    total_profiles = TOTAL_PROFILES  # Use environment variable
    total_tasks = total_profiles * (30 + 20) # Total tasks
    start_time = time.time() # Start time for the entire script

    # Pre-execution Information
    total_desktop = total_profiles * 30
    total_mobile = total_profiles * 20

    print("\n📝 Execution Summary")
    print("--------------------------------------------------")
    print(f"👥 Total users        : {total_profiles} profiles")
    print(f"💻 Desktop searches   : {total_desktop}")
    print(f"📱 Mobile searches    : {total_mobile}")
    print(f"🔍 Total searches     : {total_tasks}")
    print(f"⏳ Estimated duration : ± {(total_tasks * 10) // 60} minutes")
    print(f"🔄 Error handling     : Auto-retry enabled")
    print("--------------------------------------------------\n")

    notifier.show_toast("Bing Auto Search Tool by Ryurex Corp.",
                    f"Starting search for {total_profiles} profiles:\nDesktop: {total_desktop} | Mobile: {total_mobile}\nWith auto-retry enabled",
                    duration=10)

    try:
        for n in range(1, total_profiles + 1): # Loop through each profile
            profile = f"Profile {n}"
            run_search(profile_name=profile, is_mobile=False, total_search=30)
            run_search(profile_name=profile, is_mobile=True, total_search=20)

        # Final Results & Completion
        total_elapsed = time.time() - start_time
        end_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"\n🎉 ALL DONE! Total time: {round(total_elapsed/60, 2)} minutes | Finished at {end_time}")
        notifier.show_toast("Hey All Searches Completed • Chisato (≧◡≦)", "All searches for all profiles are completed!",
                        duration=10)
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user!")
        notifier.show_toast("Search Interrupted", 
                        "Search process was interrupted by the user.", 
                        duration=10)
