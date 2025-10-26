import os
from dotenv import load_dotenv

# --- Load .env file from same directory ---
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# --- LOGIN SYSTEM CONTROL ---
# Set to True if you want users to log in; False if you’ll use your own session.
LOGIN_SYSTEM = os.environ.get('LOGIN_SYSTEM', 'True').lower() == 'true'

# Always define STRING_SESSION so the import never fails
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# --- TELEGRAM BOT CREDENTIALS ---
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "0"))           # safer default
API_HASH = os.environ.get("API_HASH", "")

# --- ADMIN & DATABASE ---
ADMINS = int(os.environ.get("ADMINS", "6073523936"))
DB_URI = os.environ.get("DB_URI", "")                 # MongoDB connection URI
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# --- ERROR LOGGING ---
# True: send error messages to admin; False: silence errors
ERROR_MESSAGE = os.environ.get('ERROR_MESSAGE', 'True').lower() == 'true'

# --- DEBUG PRINT (optional; remove if not needed) ---
# print("Loaded config: ", API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, LOGIN_SYSTEM)