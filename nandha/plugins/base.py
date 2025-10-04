

import strings

from pyrogram import filters

from nandha import bot
from nandha.helper.decorator import only_private


@bot.on_message(filters.command('start'))
@only_private
async def start(_, message):
    m = message
    user = m.from_user
    await m.reply_text(
        text=strings.START_TEXT
    )

@bot.on_message(filters.command('help'))
@only_private
async def help(_, message):
    m = message
    user = m.from_user
    await m.reply_text(
        text=strings.HELP_TEXT

    )
