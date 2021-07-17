
import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from config import Config
from .. import *
from ..utils import *
from ..utils.modules import extra

hl = Config.HANDLER
PIC = Config.ALIVE_PIC or "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
ALIVE = Config.YOUR_NAME or "ANDENCENTO USER"
Andencento_mention = f"[{ALIVE}]"
user_mention = Andencento_mention
ver = "0.0.2"
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
async def botstarted():
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
        LOGS.info("Starting Andencento")
        LOGS.info(" Andencento Startup Completed")
      else:
        Andencento.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()
       


async def asst():
  """
  Loading Assistant From here
  """
  path = 'userbot/assistant/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      start_assistant(shortname.replace(".py", ""))

async def plugs():
  """
  Modules From here
  """
  path = "userbot/plugins/*.py"
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))


async def addons():
  extra_repo = "https://github.com/Noob-Stranger/Addons-Andencento"
  if Config.EXTRA == "True":
    try:
      os.system(f"git clone {extra_repo}")  
    except BaseException:
      pass
    LOGS.info("Installing Extra Plugins")
    path = "Addons-Andencento/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as ex:
        path2 = Path(ex.name)
        shortname = path2.stem
        extra(shortname.replace(".py", ""))
