# modules/buttons.py

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_panel():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎵 Play Commands", callback_data="play_commands")],
        [InlineKeyboardButton("👮 Admin Commands", callback_data="admin_commands")],
        [InlineKeyboardButton("👤 User Commands", callback_data="user_commands")],
        [InlineKeyboardButton("🔐 Owner Commands", callback_data="owner_commands")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ])

def back_to_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Menu", callback_data="start")]
    ])