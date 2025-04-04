import os
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telegram import Bot
import time

# Automatically download and install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Get bot token and channel ID from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Use the -100... ID

# URL to your GitHub Pages HTML file
URL = 'https://aminaghayani.github.io/studenwerk/'

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Set up Chrome WebDriver (Headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in the background without opening the browser
driver = webdriver.Chrome(options=chrome_options)

# Set of reported cities to avoid sending duplicate messages
reported_cities = set()

def check_and_send_message():
    driver.get(URL)

    # Find the <select> dropdown and options
    select = driver.find_element("id", "citySelect")
    options = select.find_elements("tag name", "option")

    available_cities = []  # List to hold available cities for printing

    # Iterate over the options and print their status
    for option in options:
        city = option.get_attribute("value")
        option_text = option.text  # Text to show in the dropdown
        is_disabled = option.get_attribute("disabled") is not None
        
        # Print the option with its disabled status
        print(f"Option: {option_text} - {'Disabled' if is_disabled else 'Enabled'}")
        
        if city and not is_disabled:  # Check if the option is enabled
            available_cities.append(city)  # Add to available cities list
            if city not in reported_cities:  # Prevent sending duplicate messages
                print(f"Sending message for {city}...")
                bot.send_message(chat_id=CHANNEL_ID, text=f"{city} ist jetzt verfügbar!")
                reported_cities.add(city)

    # Print all available cities at the end
    if available_cities:
        print(f"Available cities: {', '.join(available_cities)}")

# Run the check every 10 seconds
check_and_send_message()

# Close the driver once done
driver.quit()
