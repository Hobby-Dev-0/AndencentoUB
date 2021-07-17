
import glob
import os
import sys
from pathlib import Path
from sys import argv

import telethon.utils
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from config import Config
from .. import *
from ..utils import *
from ..utils.modules import extra
       
async def main():
       """
       START BOT
       """
       async def add_bot(bot_token):
              await bot.start(bot_token)
              Andencento.me = await bot.get_me()
              Andencento.uid = telethon.utils.get_peer_id(bot.me)
        
       if len(argv) not in (1, 3, 4):
              Andencento.disconnect()
       else:
              Andencento.tgbot = None
              if Config.BOT_TOKEN is not None:
                     print("CHECKING BOT USERNAME")
                     Andencento.tgbot = TelegramClient(
                            "TG_BOT_TOKEN",
                            api_id=Var.APP_ID,
                            api_hash=Var.API_HASH
                     ).start(bot_token=Var.BOT_TOKEN)
                     Andencento.loop.run_until_complete(add_bot(Var.BOT_TOKEN))
                     print("CHECKING SUCESS")
              else:
                     Andencento.start()


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
