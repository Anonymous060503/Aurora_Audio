# modules/admin.py

from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream, InputStream
from modules.utils import yt_stream_link

# Set your bot and voice client instance (to be initialized in main.py)
bot: Client = None
pytgcalls: PyTgCalls = None

# PLAY AUDIO
@Client.on_message(filters.command("play") & filters.group)
async def play_audio(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide a song name or YouTube link.")

    query = message.text.split(None, 1)[1]
    await message.reply_text("🔍 Searching...")

    stream_url = await yt_stream_link(query)
    if not stream_url:
        return await message.reply_text("❌ Couldn't fetch stream link.")

    await pytgcalls.join_group_call(
        message.chat.id,
        InputStream(
            InputAudioStream(
                stream_url,
            )
        ),
        stream_type="local_stream",
    )
    await message.reply_text(f"▶️ Playing: {query}")

# PLAY VIDEO
@Client.on_message(filters.command("vplay") & filters.group)
async def play_video(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide a video name or YouTube link.")

    query = message.text.split(None, 1)[1]
    await message.reply_text("🔍 Searching video...")

    stream_url = await yt_stream_link(query, video=True)
    if not stream_url:
        return await message.reply_text("❌ Couldn't fetch video link.")

    await pytgcalls.join_group_call(
        message.chat.id,
        InputStream(
            InputAudioStream(
                stream_url,
            )
        ),
        stream_type="local_stream",
    )
    await message.reply_text(f"🎥 Streaming Video: {query}")

# PAUSE
@Client.on_message(filters.command("pause") & filters.group)
async def pause_audio(_, message: Message):
    await pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("⏸️ Paused playback.")

# RESUME
@Client.on_message(filters.command("resume") & filters.group)
async def resume_audio(_, message: Message):
    await pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("▶️ Resumed playback.")

# STOP
@Client.on_message(filters.command("stop") & filters.group)
async def stop_audio(_, message: Message):
    await pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("⏹️ Stopped playback.")

# SKIP
@Client.on_message(filters.command("skip") & filters.group)
async def skip_track(_, message: Message):
    # Placeholder for skip logic
    await message.reply_text("⏭️ Skipping is not implemented yet.")