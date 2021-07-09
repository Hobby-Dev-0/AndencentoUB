import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from . import LOGS
from . import Andencento
from config import Config
from .utils import load_module


# let's get the bot ready
async def Andencento_bot(bot_token):
    try:
        await Andencento.start(bot_token)
        Andencento.me = await Andencento.get_me()
        Andencento.uid = telethon.utils.get_peer_id(Andencento.me)
    except Exception as e:
        LOGS.error(f"ANDENCENTO_SESSION - {str(e)}")
        sys.exit()


# Andencento bot starter...
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
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()
        
 
# imports plugins...
path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if len(sys.argv) not in (1, 3, 4):
    Andencento.disconnect()
else:
    Andencento.tgbot = None
    Andencento.run_until_disconnected()
