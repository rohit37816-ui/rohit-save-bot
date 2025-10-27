# user_client.py
from pyrogram import Client
from config import API_ID, API_HASH, STRING_SESSION, LOGIN_SYSTEM

TechVJUser = None

async def ensure_user_client_started():
    global TechVJUser
    if STRING_SESSION and (LOGIN_SYSTEM is False):
        if TechVJUser is None:
            TechVJUser = Client(
                "TechVJUser",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=STRING_SESSION
            )
        try:
            await TechVJUser.start()
        except Exception:
            # Already running or start race; ignore
            pass
