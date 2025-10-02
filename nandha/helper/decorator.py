
from pyrogram import filters, enums

import config

def only_private(func):
    async def wrapper(bot, message):
        if message.chat.type != enums.ChatType.PRIVATE:
            return await message.reply_text(
                text='<b>This command only work in private!</b>'
            )
        return await func(bot, message)
    
    return wrapper


def only_devs(func):
    async def wrapper(bot, message):
        user = message.from_user
        if user.id not in config.devs_list:
            return await message.reply_text(
                text='<b>This command is restricted to developers only!</b>'
            )
        return await func(bot, message)
    
    return wrapper
