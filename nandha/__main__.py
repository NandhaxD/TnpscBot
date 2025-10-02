
from nandha import bot, LOG

import strings
import config
import asyncio

from nandha.web import keep_alive, web_server
from aiohttp import web

async def start_services():        
        server = web.AppRunner(web_server())
        await server.setup()
        await web.TCPSite(server, config.BIND_ADDRESS, config.PORT).start()
        LOG.info("Web Server Initialized Successfully")
        LOG.info("=========== Service Startup Complete ===========")

        asyncio.create_task(keep_alive())
        LOG.info("Keep Alive Service Started")
        LOG.info("=========== Initializing Web Server ===========")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())
    bot.run()
    LOG.info('Bot Started!')
    with bot:
        bot.send_message(
            chat_id=f"@{config.updates}",
            text=strings.RESTARTED_TEXT
        )
