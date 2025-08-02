# modules/owner.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from modules.database import get_active_chats, clear_all_chats

# Filter only for owner
owner_filter = filters.user(OWNER_ID)

@Client.on_message(filters.command("status") & owner_filter)
async def status_handler(client: Client, message: Message):
    await message.reply("✅ Bot is up and running!")

@Client.on_message(filters.command("groups") & owner_filter)
async def groups_handler(client: Client, message: Message):
    active_chats = get_active_chats()
    if not active_chats:
        await message.reply("📭 Bot is not active in any groups.")
        return

    reply_text = "**📊 Active Groups List:**\n"
    for i, group in enumerate(active_chats, start=1):
        reply_text += f"{i}. `{group}`\n"

    await message.reply(reply_text)

@Client.on_message(filters.command("leaveall") & owner_filter)
async def leave_all_handler(client: Client, message: Message):
    active_chats = get_active_chats()
    left_count = 0

    for chat_id in active_chats:
        try:
            await client.leave_chat(int(chat_id))
            left_count += 1
        except Exception:
            pass

    clear_all_chats()
    await message.reply(f"✅ Left {left_count} groups.")

@Client.on_message(filters.command("restartbot") & owner_filter)
async def restart_handler(client: Client, message: Message):
    await message.reply("♻️ Restarting bot...")
    import os, sys
    os.execv(sys.executable, ['python'] + sys.argv)