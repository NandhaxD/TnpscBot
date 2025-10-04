
import time
import config
import io
import sys
import traceback
import subprocess


from nandha import bot
from nandha.helper.utils import get_as_document
from nandha.helper.scripts import paste

from pyrogram import filters, types, enums



async def pyroaexec(code, bot, message, m, r, chat, ruser, my):
    namespace = {}

    exec(
        "async def __pyroaexec(bot, message, m, r, chat, ruser, my): "
        + "".join(f"\n {l_}" for l_ in code.split("\n")),
        namespace
    )
    
    # Call the function from the namespace
    return await namespace["__pyroaexec"](bot, message, m, r, chat, ruser, my)



@bot.on_message(filters.user(config.dev_list) & filters.command(['pe','peval', 'eval', 'e']))
async def pyroevaluate(bot, message: types.Message):

    message = m = message 
    stime = time.time()
    if len(message.text.split()) < 2:
        return await message.reply_text(
          "🕵️ **Provide code execute...**"
    )

    msg = await message.reply("**–––> Executing code....**")
    stdout = io.StringIO()
    cmd = message.text.split(maxsplit=1)[1]

    r = m.reply_to_message
    message_id = m.id
        
    ruser = getattr(r, 'from_user', None)
    my = getattr(m, 'from_user', None)
    chat = getattr(m, 'chat', None)

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await pyroaexec(
            code=cmd, 
            bot=bot,
            message=message,
            m=message, 
            r=r,
            chat=chat,
            ruser=ruser,
            my=my
    )
    except Exception as e:
        # exc = traceback.format_exception_only(type(e), e)[-1].strip()
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()

    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""

    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "**Success** ✅"
    
    output = evaluation.strip()
    taken_time = round(time.time() - stime, 3)

    if len(output) > 4000:
        if len(cmd) > 1000:
            _paste = await paste(cmd)
            if 'error' in _paste:
                caption = "**Paste link not available at the movement.**"
            else:
                caption = _paste["paste_url"]
        else:
            caption=f"**Command**:\n{cmd}\n\n⚡ **Taken time**: `{taken_time}`"
        
        
        file = get_as_document(output)
        await msg.delete()
        await m.reply_document(
            file,
            caption=caption
        )
    else:
        await msg.edit_text(
        text = ( 
        f"**Command**:\n```py\n{cmd}```"
        f"\n\n**Output**:\n```py\n{output}```"
        f"\n\n**Taken Time**: `{taken_time}`"
        ), parse_mode=enums.ParseMode.MARKDOWN
        )



@bot.on_message(filters.user(config.dev_list) & filters.command(['shell','sh']))
async def shell(bot, message):
    
    stime = time.time()
    chat = message.chat

    message_id = message.id
        
    if not len(message.text.split()) >= 2:
        return await message.reply_text(
        text="🕵️ Provide code execute..."
    )
    cmd = message.text.split(maxsplit=1)[1]
    msg = await message.reply("**–––> Executing code....**")

    try:
        output = subprocess.getoutput(cmd)
    except Exception as e:
        output = traceback.format_exc()

    taken_time = round(time.time() - stime, 3)

    if len(output) > 4000:
        if len(cmd) > 1000:
            _paste = await paste(cmd)
            if 'error' in _paste:
                caption = "**Paste link not available at the movement.**"
            else:
                caption = _paste["paste_url"]
        else:
            caption=f"**Command**:\n{cmd}\n\n⚡ **Taken time**: `{taken_time}`"
        
        
        file = get_as_document(output)
        await msg.delete()
        await message.reply_document(
            document=file,
            caption=caption
        )
    else:
        await msg.edit_text(
        text = ( 
        f"**Command**:\n```py\n{cmd}```"
        f"\n\n**Output**:\n```py\n{output}```"
        f"\n\n**Taken Time**: `{taken_time}`"
        ), parse_mode=enums.ParseMode.MARKDOWN
    )