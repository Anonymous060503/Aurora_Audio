# modules/player.py

from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pyrogram import Client
import logging

voice_client: PyTgCalls = None

def init_voice_client(app: Client):
    global voice_client
    voice_client = PyTgCalls(app)

    @voice_client.on_stream_end()
    async def on_stream_end_handler(_, update: Update):
        chat_id = update.chat_id
        logging.info(f"Stream ended in chat {chat_id}. Leaving group call.")
        await voice_client.leave_group_call(chat_id)

    return voice_client