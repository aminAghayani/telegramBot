import os
import requests

# Get bot token and channel ID from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Use the -100... ID

# Ensure variables are set
if not BOT_TOKEN or not CHANNEL_ID:
    print("❌ Error: BOT_TOKEN or CHANNEL_ID not set.")
    exit(1)

# Message to send
message = "Hello, this is a test message from GitHub Actions to my private channel!"

# Telegram API endpoint
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Send the message
response = requests.post(url, data={
    'chat_id': CHANNEL_ID,
    'text': message
})

# Check response
if response.status_code == 200:
    print("✅ Message sent to private channel successfully!")
else:
    print(f"❌ Failed to send message: {response.status_code}")
    print(f"Response: {response.text}")  # Debugging info
