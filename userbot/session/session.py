from .. import *

from pySmartDL import SmartDL
from requests import get
from config import Config
from config import Config as Var
ALIVE_NAME = Config.YOUR_NAME
YOUR_NAME = Config.YOUR_NAME
from Config import Config
versionop = "0.0.2"
W2Hversion = versionop
botversion = versionop
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if Var.ANDENCENTO_SESSION:
    session_name = str(Var.ANDENCENTO_SESSION)
    Andencento = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    Andencento = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
