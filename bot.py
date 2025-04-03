import telegram
import time

# Replace with your bot token and channel ID
BOT_TOKEN = "7794516283:AAEp8cOhW8Nc_Iphq_7PUgb_mspCEutWZM8"
CHANNEL_ID = "-1002504539586"

bot = telegram.Bot(token=BOT_TOKEN)

def send_message():
    bot.send_message(chat_id=CHANNEL_ID, text="Hello! This is a scheduled message.")

while True:
    send_message()
    time.sleep(60)  # Wait for 1 minute
