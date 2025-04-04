import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from telegram import Bot

# Get credentials from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
URL = "https://aminaghayani.github.io/studenwerk/"

# Telegram bot init
bot = Bot(token=BOT_TOKEN)

# Set Firefox binary path (Linux default)
firefox_binary_path = "/usr/bin/firefox"
geckodriver_path = "/usr/local/bin/geckodriver"  # Location where you install it

# Setup headless Firefox
options = Options()
options.binary = FirefoxBinary(firefox_binary_path)
options.headless = True

# Start WebDriver
driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)

# Track cities already reported
reported_cities = set()

def check_and_send_message():
    driver.get(URL)
    select = driver.find_element("id", "citySelect")
    options_list = select.find_elements("tag name", "option")

    for option in options_list:
        city = option.get_attribute("value")
        label = option.text.strip()
        is_disabled = option.get_attribute("disabled") is not None

        print(f"{label} -> {'Disabled' if is_disabled else 'Enabled'}")

        if city and not is_disabled and city not in reported_cities:
            message = f"🚨 {label} ist jetzt verfügbar!"
            print(f"Sending Telegram message: {message}")
            bot.send_message(chat_id=CHANNEL_ID, text=message)
            reported_cities.add(city)

check_and_send_message()
driver.quit()
