
import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from config import Config
from . import *
from .utils import *
from .session.main import *

try:
    print ("Configuring Envoirment")
    Andencento.loop.run_until_complete(botstarted())
    LOGS.info("Envoirment is configured for bot")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

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
