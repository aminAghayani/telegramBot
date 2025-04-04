import telegram
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not BOT_TOKEN or not CHANNEL_ID:
    print("❌ Error: BOT_TOKEN or CHANNEL_ID not set.")
    exit(1)

bot = telegram.Bot(token=BOT_TOKEN)

try:
    response = bot.send_message(chat_id=CHANNEL_ID, text="Hello! This is a message from GitHub Actions.")
    print("✅ Message sent successfully!")
    print("Response:", response)  # Log the response object
except Exception as e:
    print("❌ Error sending message:", e)
