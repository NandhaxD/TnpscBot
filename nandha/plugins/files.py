
import config


from pyrogram import filters, types, enums
from nandha import bot
from nandha.helpers.decorator import only_devs
from nandha.db.files import add_file, remove_files


@bot.on_message(filters.command('addfile'))
@only_devs
async def addfile(_, message: types.Message):
        m = message
        r = m.reply_to_message
        media = [
            enums.MessageMediaType.DOCUMENT,
            enums.MessageMediaType.VIDEO,
        ]

        if len(m.text.split()) != 2:
            return await m.reply_text('/addfile [category]')


        category = m.text.split()[1]

        if r and (r.media and r.media in media):
        
            file_data = r.video or r.document
            file_name = file_data.file_name
            file_id = file_data.file_id
            file_unique_id = file_data.file_unique_id
            file_type = file_data.file_type

            file = await add_file(
                file_name=file_name,
                file_id=file_id,
                file_unique_id=file_unique_id
                file_type=file_type
            )

            if file:
                return await m.reply_text('File added successfuly.')
            else:
                return await m.reply_text('Failed to remove.')
        
        else:
            return await m.reply_text(
                    'Reply to a file e.g example a video, document'
            )



