
import config
import strings

from pyrogram import filters, types, enums
from nandha import bot
from nandha.helpers.decorator import only_devs
from nandha.db.files import add_file, remove_files
from nandha.utils import get_size, fixed_file_name


@bot.on_message(filters.command('addfile'))
@only_devs
async def addfiles(_, message: types.Message):
        m = message
        r = m.reply_to_message

        MEDIA = [
            enums.MessageMediaType.DOCUMENT,
            enums.MessageMediaType.VIDEO,
        ]

        if len(m.text.split()) != 2:
            return await m.reply_text(strings.WRONG_ADD_USAGE)


        category = str(m.text.split()[1])

        if r and (r.media and r.media in MEDIA):
        
            file_data = r.video or r.document
            file_name = file_data.file_name
            file_size = file_data.file_size
            file_id = file_data.file_id
            file_unique_id = file_data.file_unique_id
            file_type = file_data.file_type

            is_file_added = await add_file(
                file_name=file_name,
                file_id=file_id,
                file_unique_id=file_unique_id,
                file_type=file_type
            )

            if is_file_added:
                return await m.reply_text(text=strings.FILE_ADDED)
            else:
                return await m.reply_text(text=strings.FILE_REMOVED)
        
        else:
            return await m.reply_text(
                    text='<b>Reply to a Supported file format e.g Example video, document</b>'
            )



