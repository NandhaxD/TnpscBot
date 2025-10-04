import os

name = 'TNPSC_ROBOT'
bot_token = os.getenv('TOKEN', '')
bot_id = int(bot_token.split(':')[0])
support = 'NandhaSupport'
updates = 'NandhaBots'
db_channel = -100455582566

dev_list = []

WEB_SLLEP = 4*60
WEB_URL = ''
PORT = int(os.environ.get("PORT", 8080))
BIND_ADDRESS = str(os.environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))

PREFIXES = ['/', '.', '?', '$', '!']
MONGO_DB_URI = os.getenv('DB_URI', '')
MONGO_DB_NAME = 'TNPSC_ROBOT'

