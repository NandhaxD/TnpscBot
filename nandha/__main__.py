
from nandha import bot, LOG

import strings
import config
import asyncio

from nandha.web import keep_alive, web_server
from aiohttp import web


async def start_pbot():
      await bot.start()
      await bot.send_message(
            chat_id=config.support,
            text=strings.RESTARTED_TEXT
      )
      LOG.info('Bot Client Started!')

  
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
    async_funcs = [
        start_pbot(),
        start_services()
    ]
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*async_funcs))


