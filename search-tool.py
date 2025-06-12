# Import Libraries
from selenium import webdriver # WebDriver for browser automation
from selenium.webdriver.edge.service import Service # Service for Edge WebDriver
from selenium.webdriver.edge.options import Options # Options for Edge WebDriver
from selenium.webdriver.common.by import By # By class for locating elements
from selenium.webdriver.common.keys import Keys # Keys class for keyboard actions
from win10toast import ToastNotifier # ToastNotifier for Windows notifications
from tqdm import tqdm # tqdm for progress bar
import time # Time for sleep and time calculations
import random # Random for generating random keywords
import string # String for generating random suffixes
import datetime # Datetime for formatting time output

# Opening Text
print("""
************************************************************
*                                                          *
*        Welcome to the Bing Auto Search Tool V2.0!        *
*                                                          *
*           Developed by Muhammad Rafi (Ryurex)            *
*         In collaboration with Chisato Nishikigi          *
*                                                          *
*                 --  Now Update with: --                  *
*   Time Estimation | Switch Profile | Desktop & Mobile    *
*         Random Keyword Generation | Random Delay         *
*                                                          *
*     Automating your searches, One query at a time!       *
*                                                          *
************************************************************
""")

# Initial Setup
notifier = ToastNotifier() 
headless = True # Default to headless mode
detailed = False # Default to not showing detailed information

# Ask user input
headless_input = input("Do you want to inactivate headless mode (Y/N): ").strip().lower() 
if headless_input == 'y': 
    headless = False

detailed_input = input("Do you want to show detailed information (Y/N): ").strip().lower()
if detailed_input == 'y':
    detailed = True

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
    "genshin impact", "AI chatbot", "midjourney prompt", "cooking tips", "learn english"
]

# Keyword Generator
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

# Core Search Function
def run_search(profile_name, is_mobile=False, total_search=30): 
    options = Options() # Set up Edge options
    options.add_argument("--disable-gpu") # Disable GPU acceleration
    options.add_argument("--log-level=3") # Set log level to suppress logs
    # >>>>>>>>>>>>>>>>>> Set user-data-dir based on the profile name <<<<<<<<<<<<<<<<<<<<<<
    options.add_argument(r"--user-data-dir=C:\Users\<YOUR USERNAME>\AppData\Local\Microsoft\Edge\User Data\Ryurex Project") # Set user data directory
    options.add_argument(f"--profile-directory={profile_name}") # Set profile directory

    if headless: # If headless mode is enabled
        options.add_argument("--headless=new")

    if is_mobile: # If mobile emulation is enabled
        mobile_emulation = {"deviceName": "iPhone X"} # Use iPhone X emulation
        options.add_experimental_option("mobileEmulation", mobile_emulation) # Add mobile emulation option

    print(f"🚀 Starting search | Profile: {profile_name} | Mode: {'Mobile' if is_mobile else 'Desktop'} | Headless: {headless}")

    driver = webdriver.Edge(service=Service(), options=options) # Initialize Edge WebDriver with options

    try:
        delay_per_search = [] # List to store delay times for each search
        pbar = tqdm(range(total_search), desc=f"{profile_name} - {'Mobile' if is_mobile else 'Desktop'}", ncols=120 if detailed else 80)

        for i in pbar: # Loop through the number of searches
            mode = random.choice(['short', 'normal', 'long'])
            keyword = generate_random_keyword(mode)

            start = time.time() # Start time for the search
            driver.get("https://www.bing.com") # Open Bing homepage
            time.sleep(2) # Wait for the page to load
            search_box = driver.find_element(By.NAME, "q") # Find the search box element
            search_box.clear() # Clear the search box
            search_box.send_keys(keyword) # Enter the keyword into the search box
            search_box.send_keys(Keys.RETURN) # Press Enter to submit the search

            wait_time = random.randint(8, 12) # Random wait time between 8 to 12 seconds
            if detailed: # If detailed mode is enabled, show more information
                pbar.set_postfix({"Keyword": keyword[:25], "Delay": f"{wait_time}s"}) 
            time.sleep(wait_time) # Wait for the search results to load
            end = time.time() # End time for the search
            delay_per_search.append(end - start) # Calculate the delay for this search

        avg_time = sum(delay_per_search) / len(delay_per_search) # Calculate average time per search
        est_total = avg_time * total_search # Estimate total time for all searches
        notifier.show_toast("Bing Search Done", 
                            f"{profile_name} - {'Mobile' if is_mobile else 'Desktop'} selesai!",
                            duration=5) # Show notification when search is done

        print(f"✅ Completed {profile_name} ({'Mobile' if is_mobile else 'Desktop'}) | Estimated: {round(est_total/60, 1)} minutes")
    except Exception as e:
        print(f"⚠️ Error on {profile_name}: {e}")
    finally:
        driver.quit() # Close the WebDriver
        time.sleep(2) # Wait for a short time before the next search

# Master Runner
if __name__ == "__main__": 
    total_profiles = 11 # >>>>>>>>>>>>>>>>>(Change this to the number of profiles you want to search)<<<<<<<<<<<<<<<<<<<<<<<<<<
    total_tasks = total_profiles * (30 + 20) # Total tasks
    start_time = time.time() # Start time for the entire script

    print(f"\n📌 Total searches: {total_tasks} (Desktop: 300 + Mobile: 200)")
    print(f"⏳ Estimated total time: ± {(total_tasks * 10) // 60} minutes")
    notifier.show_toast("Bing Auto Search Tool by Ryurex Corp.",
                        f"Starting search for {total_profiles} profiles, total {total_tasks} searches.",
                        duration=10)

    for n in range(1, total_profiles + 1): # Loop through each profile
        profile = f"Profile {n}" 
        run_search(profile_name=profile, is_mobile=False, total_search=30)
        run_search(profile_name=profile, is_mobile=True, total_search=20)

    total_elapsed = time.time() - start_time # Calculate total elapsed time
    end_time = datetime.datetime.now().strftime('%H:%M:%S') # Format end time

    print(f"\n🎉 ALL DONE! Total time: {round(total_elapsed/60, 2)} minutes | Finished at {end_time}")
    notifier.show_toast("Hey All Searches Completed • Chisato (≧◡≦)", "All searches for all profiles are completed!",
                        duration=10) # Show final notification
