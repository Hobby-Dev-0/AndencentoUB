
import glob
import os
import sys
from pathlib import Path
from sys import argv

import telethon.utils
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from config import Config
from . import *
from .utils import *
from .session.main import *

hl = Config.HANDLER
PIC = Config.ALIVE_PIC or "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
ALIVE = Config.YOUR_NAME or "ANDENCENTO USER"
Andencento_mention = f"[{ALIVE}]"
user_mention = Andencento_mention
ver = "0.0.2"
# let's get the bot ready
                    
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.BOT_TOKEN is not None:
        print("CHECKING BOT USERNAME")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("CHECKING SUCESS")
    else:
        bot.start()

async def mod():
    await asst()
    await plugs()
    await addons()


Andencento.loop.run_until_complete(mod())

async def op():
    await Andencento(JoinChannelRequest("Andencento"))
    await Andencento(JoinChannelRequest("AndencentoSupport"))
        
Andencento.loop.create_task(op())

async def Andencentoiosop():
    try:
        if Config.LOGGER_ID != 0:
            await bot.tgbot.send_file(
                Config.LOGGER_ID,
                PIC,
                caption=f"#START \n\nDeployed Andencento Successfully\n\n**Andencento - {ver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [Andencneto Channel](t.me\n\n /Andencento) for Updates & [Andencento Chat](t.me/AndencentoSupport) for any query regarding Team Andencento",
            )
    except Exception as e:
        LOGS.info(str(e))



Andencento.loop.create_task(Andencentoiosop())
print("Andencento Deployed And Working Fine")

if len(sys.argv) not in (1, 3, 4):
    Andencento.disconnect()
else:
    Andencento.run_until_disconnected()
    noob.run_until_disconnected()
