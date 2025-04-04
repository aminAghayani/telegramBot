import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Read environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not BOT_TOKEN or not CHANNEL_ID:
    print("❌ Error: BOT_TOKEN or CHANNEL_ID not set.")
    exit(1)

# Initialize the bot and the updater
updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Function to handle incoming messages
def forward_to_channel(update: Update, context: CallbackContext):
    # Get the message text from the user
    message = update.message.text
    # Send the message to the channel
    context.bot.send_message(chat_id=CHANNEL_ID, text=message)

# Add a message handler to forward all messages to the channel
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_to_channel))

# Start the bot
updater.start_polling()
updater.idle()
