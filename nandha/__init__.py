
from pyrogram import Client, enums
from motor.motor_asyncio import AsyncIOMotorClient
from nandha.fonts import Fonts

import config
import logging


LOG = logging.getLogger(__name__)



font = Fonts.sim


bot = Client(
    name='Tnpsc-Robot',
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token,
    parse_mode=enums.ParseMode.HTML
)

try:
    db_client = AsyncIOMotorClient(config.MONGO_DB_URI)
    database = db_client[config.MONGO_DB_NAME]
except Exception as e:
    LOG.error(f'> While connecting to mongodb ... there was error found: {e}')




