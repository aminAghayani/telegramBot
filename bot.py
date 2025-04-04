import os
import requests

# Get the bot token and the user ID from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

# Define the message you want to send
message = "Hello, this is a message sent from GitHub Action!"

# Construct the URL to send the message to your bot
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Make the API request
response = requests.post(url, data={
    'chat_id': USER_ID,
    'text': message
})

# Check the response
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message: {response.status_code}")
