# modules/database.py

# You can replace this with MongoDB/Redis later if needed
active_chats = set()

def add_active_chat(chat_id: int):
    active_chats.add(chat_id)

def remove_active_chat(chat_id: int):
    active_chats.discard(chat_id)

def get_active_chats():
    return list(active_chats)

def clear_all_chats():
    active_chats.clear()