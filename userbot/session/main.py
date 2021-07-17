
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

