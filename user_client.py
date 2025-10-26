# user_client.py
from pyrogram import Client
from config import API_ID, API_HASH, STRING_SESSION, LOGIN_SYSTEM

TechVJUser = None

async def ensure_user_client_started():
    global TechVJUser

    # Skip if no string session or login system enabled
    if not STRING_SESSION or LOGIN_SYSTEM:
        return None

    # Initialize client if not created yet
    if TechVJUser is None:
        TechVJUser = Client(
            "TechVJUser",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=STRING_SESSION
        )

    # Ensure client is started before returning
    if not TechVJUser.is_connected:
        try:
            await TechVJUser.start()
            print("✅ User client started successfully.")
        except Exception as e:
            print(f"⚠️ Failed to start user client: {e}")
            TechVJUser = None
            return None

    return TechVJUser
