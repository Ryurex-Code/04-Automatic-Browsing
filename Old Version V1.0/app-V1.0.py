#Import Libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from win10toast import ToastNotifier
import time

# Opening text for the Bing Auto Search Tool
opening_text = """
************************************************************
*                                                          *
*       Welcome to the Bing Auto Search Tool V1.0!         *
*                                                          *
*           Developed by Muhammad Rafi (Ryurex)            *
*         In collaboration with Chisato Nishikigi          *
*                                                          *
*     Automating your searches, one query at a time!       *
*                                                          *
************************************************************
"""
print(opening_text)

# Initialize Windows toast notification
notifier = ToastNotifier()

# Setup Edge WebDriver
service = Service() # Use the default path for Edge WebDriver
options = Options() # Create an instance of Options
options.add_argument("--headless=new")  # Run browser in headless mode
options.add_argument("--disable-gpu")  # Disable GPU acceleration
options.add_argument("--log-level=3")  # Suppress logs

driver = webdriver.Edge(service=service, options=options) # Initialize Edge WebDriver

# List of keywords to search
keywords = [
    "weather today", "news headlines", "how to cook pasta", "best movies 2025", "healthy habits",
    "space exploration", "latest technology", "travel destinations", "exercise tips", "mindfulness meditation",
    "stock market updates", "python programming", "world history facts", "funny memes", "top music hits",
    "gardening ideas", "car maintenance tips", "healthy recipes", "dog training", "cat breeds",
    "digital marketing", "artificial intelligence", "climate change", "movie reviews", "book recommendations",
    "photography tips", "home decoration", "language learning", "self improvement", "Chisato Nishikigi"
]

try:
    total_searches = 30 # Total number of searches to perform
    for i in range(total_searches):
        keyword = keywords[i % len(keywords)]
        driver.get("https://www.bing.com")
        time.sleep(2) # Wait for the page to load

        search_box = driver.find_element(By.NAME, "q") # Locate the search box
        search_box.clear() 
        search_box.send_keys(keyword)  
        search_box.send_keys(Keys.RETURN)  # Submit the search

        print(f"🔍 Search #{i + 1}/{total_searches}: {keyword}") 
        time.sleep(10) # Wait for the search results to load

    print("✅ Completed 30 searches successfully.")
    notifier.show_toast("Bing Auto Search Task Complete", "The program has completed all searches successfully.", duration=5)

except Exception as e:
    print(f"⚠️ An error occurred: {e}")

finally:
    driver.quit()
