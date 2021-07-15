import os
import sys
import time
from distutils.util import strtobool as sb
# Temprorary Purpose Soon will be remoced
op = os.environ.get("REQ", None)
if {op} == "False" or None:
    try:
        os.system("pip install -r requirements.txt")
    except BaseException:
        pass
from logging import DEBUG, INFO, basicConfig, getLogger
import heroku3
from dotenv import load_dotenv
import time
from .session import *
from .session import bot
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession
ENV = os.environ.get("ENV", False)
import pylast
from pySmartDL import SmartDL
from requests import get
from config import Config
from config import Config as Var
ALIVE_NAME = Config.YOUR_NAME
StartTime = time.time()
YOUR_NAME = Config.YOUR_NAME
from Config import Config
versionop = "0.0.2"
W2Hversion = versionop
botversion = versionop
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
from .session import Andencento


noob = TelegramClient(None, Var.APP_ID, Var.API_HASH)
BIO_MSG = os.environ.get("BIO_MSG", None)

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

   # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    COMMAND_HAND_LER = os.environ.get("HANDLER", ".")

    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # FedBan Premium Module
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)

# Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

   
    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    REDIRECTCHANNEL = os.environ.get("REDIRECTCHANNEL", None)

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", "India"))

    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    
    # Custom Module
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                      api_secret=LASTFM_SECRET,
                                      username=LASTFM_USERNAME,
                                      password_hash=LASTFM_PASS)
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
else:
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)



# global variables
CMD_LIST = {}
# for later purposes
CMD_HELP = {}
CMD_HELP_BOT = {}
BRAIN_CHECKER = []
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}
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


from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio

import pylast
from pySmartDL import SmartDL
from requests import get
# Bot Logs setup:
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger("ANDENCENTO")

    # Check if the config was edited by using the already used variable.
    # Basically, its the 'virginity check' for the config file ;)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    PATTERNS = os.environ.get("PATTERNS", ".;!,")
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
    
    # Custom Module
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    PATTERNS = os.environ.get("PATTERNS", ".;!,")
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
  
    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # FedBan Premium Module
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)

    #make by LEGEND X 
    botnickname = os.environ.get("BOT_NICK_NAME", None)

# Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

   
    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    REDIRECTCHANNEL = os.environ.get("REDIRECTCHANNEL", None)

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", "India"))

    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    
    # Custom Module
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)

    # Upstream Repo
    UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/TeamExtremePro/ExtremeProUserbot")

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                      api_secret=LASTFM_SECRET,
                                      username=LASTFM_USERNAME,
                                      password_hash=LASTFM_PASS)
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
else:
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)
