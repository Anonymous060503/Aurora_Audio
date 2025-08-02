from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN
from modules import admin, user, owner, player, buttons
import logging
import asyncio

# Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Bot
bot = Client(
    "AuroraBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="modules")
)

# Start Message (Handled inside user.py, optional override here)
@bot.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    await message.reply_text(
        "**👋 Welcome to Aurora HD Music Bot!**\n\n"
        "Use this bot in a group to play music in HD quality.\n\n"
        "__For help, use /help or press the buttons below.__",
        reply_markup=buttons.start_panel()
    )

# Run the Bot
if __name__ == "__main__":
    logger.info(">> Aurora HD Bot is starting...")
    bot.run()