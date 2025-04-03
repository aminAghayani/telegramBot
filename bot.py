import telegram
import time

# Replace with your bot token and channel ID
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "YOUR_CHANNEL_ID"

bot = telegram.Bot(token=BOT_TOKEN)

def send_message():
    bot.send_message(chat_id=CHANNEL_ID, text="Hello! This is a scheduled message.")

while True:
    send_message()
    time.sleep(60)  # Wait for 1 minute
