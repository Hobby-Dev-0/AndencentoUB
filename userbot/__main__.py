import glob
from userbot import Andencento
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from . import *
from var import Var
from .utils import load_module
from .utils import start_assistant
from . import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils



                    
async def add_bot(bot_token):
    await Andencento.start(bot_token)
    Andencento.me = await Andencento.get_me() 
    Andencento.uid = telethon.utils.get_peer_id(Andencento.me)



if len(sys.argv) not in (1, 3, 4):
    Andencento.disconnect()
else:
    Andencento.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            Andencento.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info(" Starting Andencento")
            Andencento.loop.run_until_complete(Andencento_bot(Config.BOT_USERNAME))
            LOGS.info(" Andencento Startup Completed")
        else:
            Andencento.start()


print("Andencento Deployed And Working Fine For Assistance")



if len(argv) not in (1, 3, 4):
    Andencento.disconnect()
else:
    Andencento.run_until_disconnected()
