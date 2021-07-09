import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from . import LOGS
from . import Andencento as bot
from config import Config
from .utils import load_module
Andencentover = "0.1
hl = Config.HANDLER
Andencento_PIC = Config.ALIVE_PIC or None

# let's get the bot ready
async def Andencento_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"ANDENCENTO_SESSION - {str(e)}")
        sys.exit()


# Andencento bot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info(" Starting Andencento")
            bot.loop.run_until_complete(Andencento_bot(Config.BOT_USERNAME))
            LOGS.info(" Andencento Startup Completed")
        else:
            bot.start()
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

# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your ANDENCENTO UB Is Now Working ⚡")
LOGS.info(
    "Head to @Andencento for Updates. Also join chat group to get help regarding to Ⱥղժҽղçҽղէօ."
)

# that's life...
async def Andencento_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                Eiva_PIC,
                caption=f"#START \n\nDeployed Ⱥղժҽղçҽղէօ Successfully\n\n**Ⱥղժҽղçҽղէօ - {Andencentover}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [Andencento Channel](t.me/Andencento) for Updates & [Andencento Chat](t.me/AndencentoSupport) for any query regarding Andencentobot",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join Andencento Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Andencento"))
    except BaseException:
        pass


bot.loop.create_task(Andencento_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
