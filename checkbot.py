import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from telegram import Bot

# Environment variables from GitHub Secrets
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

URL = 'https://aminaghayani.github.io/studenwerk/'

bot = Bot(token=BOT_TOKEN)

# Set up Firefox in headless mode
firefox_binary_path = "/usr/bin/firefox"
options = Options()
options.binary_location = firefox_binary_path
options.add_argument("--headless")

service = FirefoxService()
driver = webdriver.Firefox(service=service, options=options)

reported_cities = set()

def check_and_send_message():
    driver.get(URL)

    select = driver.find_element("id", "citySelect")
    options = select.find_elements("tag name", "option")

    available_cities = []

    for option in options:
        city = option.get_attribute("value")
        option_text = option.text
        is_disabled = option.get_attribute("disabled") is not None

        print(f"Option: {option_text} - {'Disabled' if is_disabled else 'Enabled'}")

        if city and not is_disabled:
            available_cities.append(city)
            if city not in reported_cities:
                print(f"Sending message for {city}...")
                bot.send_message(chat_id=CHANNEL_ID, text=f"{city} ist jetzt verfügbar!")
                reported_cities.add(city)

    if available_cities:
        print(f"Available cities: {', '.join(available_cities)}")

check_and_send_message()
driver.quit()
