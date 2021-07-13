import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
import heroku3
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession
ENV = os.environ.get("ENV", False)

from config import Config
from config import Config as Var
ALIVE_NAME = Config.YOUR_NAME
StartTime = time.time()

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if Var.ANDENCENTO_SESSION:
    session_name = str(Var.ANDENCENTO_SESSION)
    Andencento = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    Andencento = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)

noob = TelegramClient("noob", Var.APP_ID, Var.API_HASH)


if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger("ANDENCENTO")


try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None


bot = Andencento


# global variables
CMD_LIST = {}
CMD_HELP = {}
CMD_HELP_BOT = {}
BRAIN_CHECKER = []
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}

import os

COMMAND_HAND_LER = os.environ.get("HANDLER", ".")

#################################################################################################################

class CmdHelp:
    """
    The class I wrote to better generate command aids.
    """

    FILE = ""
    ORIGINAL_FILE = ""
    FILE_AUTHOR = ""
    IS_OFFICIAL = True
    COMMANDS = {}
    PREFIX = COMMAND_HAND_LER
    WARNING = ""
    INFO = ""

    def __init__(self, file: str, official: bool = True, file_name: str = None):
        self.FILE = file
        self.ORIGINAL_FILE = file
        self.IS_OFFICIAL = official
        self.FILE_NAME = file_name if not file_name == None else file + ".py"
        self.COMMANDS = {}
        self.FILE_AUTHOR = ""
        self.WARNING = ""
        self.INFO = ""

    def set_file_info(self, name: str, value: str):
        if name == "name":
            self.FILE = value
        elif name == "author":
            self.FILE_AUTHOR = value
        return self

    def add_command(self, command: str, params=None, usage: str = "", example=None):
        """
        Inserts commands..
        """

        self.COMMANDS[command] = {
            "command": command,
            "params": params,
            "usage": usage,
            "example": example,
        }
        return self

    def add_warning(self, warning):
        self.WARNING = warning
        return self

    def add_info(self, info):
        self.INFO = info
        return self

    def get_result(self):
        """
        Brings results.
        """

        result = f"**📗 File :** `{self.FILE}`\n"
        if self.WARNING == "" and self.INFO == "":
            result += f"**⬇️ Official:** {'✅' if self.IS_OFFICIAL else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if self.IS_OFFICIAL else '❌'}\n"

            if self.INFO == "":
                if not self.WARNING == "":
                    result += f"**⚠️ Warning :** {self.WARNING}\n\n"
            else:
                if not self.WARNING == "":
                    result += f"**⚠️ Warning :** {self.WARNING}\n"
                result += f"**ℹ️ Info:** {self.INFO}\n\n"

        for command in self.COMMANDS:
            command = self.COMMANDS[command]
            if command["params"] == None:
                result += f"**🛠 Command :** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
            else:
                result += f"**🛠 Command :** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

            if command["example"] == None:
                result += f"**💬 Details :** `{command['usage']}`\n\n"
            else:
                result += f"**💬 Details :** `{command['usage']}`\n"
                result += (
                    f"**⌨️ For Example :** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
                )
        return result

    def add(self):
        """
        Directly adds CMD_HELP.
        """
        CMD_HELP_BOT[self.FILE] = {
            "info": {
                "official": self.IS_OFFICIAL,
                "warning": self.WARNING,
                "info": self.INFO,
            },
            "commands": self.COMMANDS,
        }
        CMD_HELP[self.FILE] = self.get_result()
        return True

    def getText(self, text: str):
        if text == "REPLY_OR_USERNAME":
            return "<user name> <user name/answer >"
        elif text == "OR":
            return "or"
        elif text == "USERNAMES":
            return "<user name (s)>"






import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from config import Config
from .utils import *
from .utils.modules import extra


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
        

path = 'userbot/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))   



# Extra Modules...
extra_repo = Config.EXTRA_REPO or "https://github.com/Noob-Stranger/Addons-Andencento"
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



# imports plugins...
path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

async def op():
    await Andencento(JoinChannelRequest("Andencento"))
    await Andencento(JoinChannelRequest("AndencentoSupport"))
        
Andencento.loop.create_task(op())

print("Andencento Deployed And Working Fine")

if len(sys.argv) not in (1, 3, 4):
    Andencento.disconnect()
else:
    Andencento.tgbot = None
    Andencento.run_until_disconnected()
    
if __name__=="__main__":
    noob.run_until_disconnected()
