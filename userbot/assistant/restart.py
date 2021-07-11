import asyncio
import math
import os
import heroku3
import requests
import urllib3
import sys
from os import execl
from time import sleep

from . import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
lg_id = Config.LOGGER_ID

async def restart(event):
    if HEROKU_APP_NAME and HEROKU_API_KEY:
        try:
            Heroku
        except BaseException:
            return await tgbot.send_message(
                event, "`HEROKU_API_KEY` is wrong. Re-Check in config vars."
            )
        await tgbot.send_message(event, f"✅ **Restarted Dynos** \n**Type** `{hl}ping` **after 1 minute to check if I am working !**")
        app = Heroku.apps()[HEROKU_APP_NAME]
        app.restart()
    else:
        execl(executable, executable, "bash", "start.sh")
        
        
@tgbot.on(events.NewMessage(pattern="^/id"))
async def re(user):
    if user.reply_to_msg_id:
      await event.get_input_chat()
      r_msg = await event.get_reply_message()
      if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
              event.chat_id,
              "restarting dyno"
                if HEROKU_API_KEY:
                await restart(event)
           else:
                await tgbot.send_message("Please Set Your `HEROKU_API_KEY` to restart ᴀɴᴅᴇɴᴄᴇɴᴛᴏ")
