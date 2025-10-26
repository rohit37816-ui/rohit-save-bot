import os
from dotenv import load_dotenv

# --- Load .env file from same directory ---
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# --- LOGIN SYSTEM CONTROL ---
# Set to True if you want users to log in; False if you’ll use your own session.
LOGIN_SYSTEM = os.environ.get('LOGIN_SYSTEM', 'True').lower() == 'true'

# Always define STRING_SESSION so the import never fails
STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIwBu0eJzjYXiIZFT855fYLU1r7idwoQIp8wDtTcuGCd1EsqznDKk1baqly0aMKUtCR7nO6DMFLXqJi7fgrLtrvdcfoQ8I5eNCQLEIkmcWkozpvT3ZxjcDDoZnDLdPrIF6L_Q3Y_VvekZWd8YWYgunMcKb-9B9oTVxbpCPt-EnGp1EirTQ4y2OPtWxumv2XMN0VK1AXhnZ7Gtxdr3n4mToG-NXS07ilaCBFeRhT7UWka1-lJy59iZiDzqzMqyJkCip_nDMKTbouTunqjym8U60_a8Qm_YqQ5V_zHQnqzYF3WX1YLVEGisiyRegJ5XDucdOYJ7M7UP0bFgY1JJPdwsFHJsMI=")

# --- TELEGRAM BOT CREDENTIALS ---
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8479055966:AAEgmGioIw9EHhO0Xo2E_97hOSMMmwY9D0w")
API_ID = int(os.environ.get("API_ID", "28803298"))           # safer default
API_HASH = os.environ.get("API_HASH", "d8ea0f3e56c55b8ef9c0e8cb39b9c857")

# --- ADMIN & DATABASE ---
ADMINS = int(os.environ.get("ADMINS", "6065778458"))
DB_URI = os.environ.get("DB_URI", "")                 # MongoDB connection URI
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# --- ERROR LOGGING ---
# True: send error messages to admin; False: silence errors
ERROR_MESSAGE = os.environ.get('ERROR_MESSAGE', 'True').lower() == 'true'

# --- DEBUG PRINT (optional; remove if not needed) ---
# print("Loaded config: ", API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, LOGIN_SYSTEM)
