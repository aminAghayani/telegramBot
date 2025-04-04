import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from telegram import Bot

# Get credentials from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Should be something like -1001234567890
URL = "https://aminaghayani.github.io/studenwerk/"

# Initialize Telegram Bot
bot = Bot(token=BOT_TOKEN)

# Configure Firefox to run headless (no GUI needed)
options = webdriver.FirefoxOptions()
options.headless = True

# Start Firefox WebDriver
driver = webdriver.Firefox(options=options)

# Keep track of cities we've already sent alerts for
reported_cities = set()

def check_and_send_message():
    driver.get(URL)

    # Find the dropdown
    select = driver.find_element("id", "citySelect")
    option_elements = select.find_elements("tag name", "option")

    available_cities = []

    for option in option_elements:
        city_value = option.get_attribute("value")
        city_label = option.text.strip()
        is_disabled = option.get_attribute("disabled") is not None

        print(f"City: {city_label} -> {'Disabled' if is_disabled else 'Enabled'}")

        # Skip empty value or disabled cities
        if city_value and not is_disabled:
            available_cities.append(city_value)

            if city_value not in reported_cities:
                # Send a Telegram message
                message = f"🚨 {city_label} ist jetzt verfügbar!"
                print(f"Sending Telegram message: {message}")
                bot.send_message(chat_id=CHANNEL_ID, text=message)
                reported_cities.add(city_value)

    if not available_cities:
        print("No available cities at this time.")

# Run the check
check_and_send_message()

# Clean up
driver.quit()
