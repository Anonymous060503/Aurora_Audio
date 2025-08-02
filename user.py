# modules/user.py

from pyrogram import Client, filters
from pyrogram.types import Message
from modules.player import player
from modules.buttons import help_buttons
from modules.utils import extract_query

@Client.on_message(filters.command(["play", "vplay"]) & filters.group)
async def play_handler(client: Client, message: Message):
    query = extract_query(message)
    if not query:
        await message.reply("❌ Please provide a song name or YouTube URL.\n\nExample: `/play Alone`", quote=True)
        return

    is_video = message.text.startswith("/vplay")
    await player.enqueue(message, query, video=is_video)

@Client.on_message(filters.command("help") & filters.group)
async def help_handler(client: Client, message: Message):
    await message.reply(
        "**🎧 Aurora Audio Bot Help**",
        reply_markup=help_buttons()
    )