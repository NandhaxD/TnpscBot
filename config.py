import os


name = 'TNPSC_ROBOT'
bot_token = os.getenv('TOKEN', '')
api_id = int(os.getenv('API_ID', 6))
api_hash = os.getenv('API_HASH', 'eb06d4abfb49dc3eeb1aeb98ae0f581e')

bot_id = int(bot_token.split(':')[0])
support = 'NandhaSupport'
updates = 'NandhaBots'
db_channel = -100455582566

dev_list = [5696053228, 5696053228]

WEB_SLLEP = 4*60
WEB_URL = 'https://tnpscbot.onrender.com/'
PORT = int(os.environ.get("PORT", 8080))
BIND_ADDRESS = str(os.environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))

PREFIXES = ['/', '.', '?', '$', '!']
MONGO_DB_URI = os.getenv('DB_URI', '')
MONGO_DB_NAME = 'TNPSC_ROBOT'

