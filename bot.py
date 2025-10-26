# bot.py
# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):
    def __init__(self):
        super().__init__(
            "techvj_bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            # Flood control: lower workers, higher sleep_threshold
            workers=int(os.environ.get("PYRO_WORKERS", "8")),              # was 150
            sleep_threshold=int(os.environ.get("PYRO_SLEEP_THRESHOLD", "60"))  # was 5
        )

    async def start(self):
        # Start optional user client first (if configured)
        try:
            from user_client import ensure_user_client_started
            await ensure_user_client_started()
        except Exception:
            pass
        await super().start()
        print("✅ Bot Started — Powered By @VJ_Botz")

    async def stop(self, *args):
        await super().stop()
        print("🛑 Bot Stopped — Goodbye!")

if __name__ == "__main__":
    Bot().run()
