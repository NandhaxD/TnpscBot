import os


name = 'TNPSC_ROBOT'
bot_token = os.getenv('TOKEN', '')
api_id = int(os.getenv('API_ID', 13257951))
api_hash = os.getenv('API_HASH', 'd8ea642aedb736d40035bc05f0cfd477')

bot_id = int(bot_token.split(':')[0])
support = 'NandhaSupport'
updates = 'NandhaBots'
db_channel = -100455582566

dev_list = [5696053228, 5696053228]

WEB_SLLEP = 3*60
WEB_URL = 'https://tnpscbot.onrender.com/'
PORT = int(os.environ.get("PORT", 8080))
BIND_ADDRESS = str(os.environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))

PREFIXES = ['/', '.', '?', '$', '!']
MONGO_DB_URI = os.getenv('DB_URI', '')
MONGO_DB_NAME = 'TNPSC_ROBOT'

