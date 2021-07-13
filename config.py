import os
from telethon.tl.types import ChatBannedRights


class Config(object):
    LOGGER = True
    ABUSE = os.environ.get("ABUSE", None)
    ALIVE_MSG = os.environ.get("ALIVE_MSG", "Ⱥղժҽղçҽղէօ")
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None,
        view_messages=None,
        send_messages=True
    )
    API_HASH = os.environ.get("API_HASH", None)
    COMMAND_HAND_LER = os.environ.get("HANDLER", ".")
    APP_ID = os.environ.get("APP_ID", None)
    ANDENCENTO_SESSION = os.environ.get("ANDENCENTO_SESSION", None)
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
        t_file = open(TMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    BIO_MSG = os.environ.get("BIO_MSG", "Ⱥղժҽղçҽղէօ")
    BL_CHAT = set(int(x) for x in os.environ.get("BL_CHAT", "").split())
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    BUTTONS_IN_HELP = int(os.environ.get("BUTTONS_IN_HELP", 7))
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    SUDO_COMMAND_HAND_LER = os.environ.get("HANDLER", ".")
    DUAL_LOG = os.environ.get("DUAL_LOG", None)
    EMOJI_IN_HELP = os.environ.get("EMOJI_IN_HELP", " ")
    FBAN_LOG_GROUP = os.environ.get("FBAN_LOG_GROUP", None)
    EXTRA = os.environ.get("EXTRA", None)
    EXTRA_REPO = os.environ.get("EXTRA_REPO", None)
    if FBAN_LOG_GROUP:
        FBAN_LOG_GROUP = int(FBAN_LOG_GROUP)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GBAN_LOG_GROUP = os.environ.get("GBAN_LOG_GROUP", None)
    if GBAN_LOG_GROUP:
        GBAN_LOG_GROUP = int(GBAN_LOG_GROUP)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    ANDENCENTO_HNDLR = os.environ.get("ANDENCENTO_HNDLR", ".")
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    GROUP_REG_SED_EX_BOT_S = os.environ.get("GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)Andencento")
    HANDLER = os.environ.get("HANDLER", r"\.")
    HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    INSTANT_BLOCK = os.environ.get("INSTANT_BLOCK", "DISABLE")
    LOCATION = os.environ.get("LOCATION", None)
    LOGGER_ID = os.environ.get("LOGGER_ID", None)
    if LOGGER_ID:
        LOGGER_ID = int(LOGGER_ID)
    LYDIA_API = os.environ.get("LYDIA_API", None)
    MAX_ANTI_FLOOD_MESSAGES = 10
    MAX_MESSAGE_SIZE_LIMIT = 4095
    MAX_SPAM = int(os.environ.get("MAX_SPAM", 3))
    MONGO_URI = os.environ.get("MONGO_URI", None)
    MY_CHANNEL = os.environ.get("YOUR_CHANNEL", "Andencento")
    MY_GROUP = os.environ.get("YOUR_GROUP", "AndencentoSupport")
    OCR_API = os.environ.get("OCR_API", None)
    PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", -100)
    if PLUGIN_CHANNEL:
        PLUGIN_CHANNEL = int(PLUGIN_CHANNEL)
    PM_LOG_ID = os.environ.get("PM_LOG_ID", None)
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PM_LOG_ID", None)
    if PM_LOG_ID:
        PM_LOG_ID = int(PM_LOG_ID)
    PM_PERMIT = os.environ.get("PM_PERMIT", "ENABLE")
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
    REMOVE_BG_API = os.environ.get("REMOVE_BG_API", None)
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    STICKER_PACKNAME = os.environ.get("STICKER_PACKNAME", None)
    SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"\.")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_HANDLER", r"\.")
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    TAG_LOGGER = os.environ.get("TAG_LOGGER", None)
    if TAG_LOGGER: 
        TAG_LOGGER = int(TAG_LOGGER)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "AndencentoBot")
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    TZ = os.environ.get("TZ", "Asia/Kolkata")
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/Team-Andencento/Andencento")
    WEATHER_API = os.environ.get("WEATHER_API", None)
    YOUR_NAME = os.environ.get("YOUR_NAME", None)
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        # Get this value from my.telegram.org! Please do not steal
    LOCATION = os.environ.get("LOCATION", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
        # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "userbot")
        # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        # Send .get_id in any group with all your administration bots (added)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001169892177))
        # TG API limit. An album can have atmost 10 media!
    FBAN_LOGGER_GROUP = os.environ.get("FBAN_LOGGER_GROUP", None)

    GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # MIRROR ACE API KEY AND TOKEN
    MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", None)
    MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_KEY", None)
        # Telegram BOT Token from @BotFather
        #spootifie
        #log
        # set blacklist_chats where you do not want userbot's features
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
        # maximum number of messages for antiflood
    MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
    # providing usernames means an additional overhead for the user
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBo
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs.
    SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True

    
    
import os
from telethon.tl.types import ChatBannedRights
class Var(object):
    LOGGER = True
    ABUSE = os.environ.get("ABUSE", None)
    ALIVE_MSG = os.environ.get("ALIVE_MSG", "Ⱥղժҽղçҽղէօ")
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None,
        view_messages=None,
        send_messages=True
    )
    API_HASH = os.environ.get("API_HASH", None)
    APP_ID = os.environ.get("APP_ID", None)
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
    ANDENCENTO_SESSION = os.environ.get("ANDENCENTO_SESSION", None)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
        t_file = open(TMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    BIO_MSG = os.environ.get("BIO_MSG", "Ⱥղժҽղçҽղէօ")
    BL_CHAT = set(int(x) for x in os.environ.get("BL_CHAT", "").split())
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    BUTTONS_IN_HELP = int(os.environ.get("BUTTONS_IN_HELP", 7))
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    DUAL_LOG = os.environ.get("DUAL_LOG", None)
    EMOJI_IN_HELP = os.environ.get("EMOJI_IN_HELP", " ")
    FBAN_LOG_GROUP = os.environ.get("FBAN_LOG_GROUP", None)
    if FBAN_LOG_GROUP:
        FBAN_LOG_GROUP = int(FBAN_LOG_GROUP)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GBAN_LOG_GROUP = os.environ.get("GBAN_LOG_GROUP", None)
    if GBAN_LOG_GROUP:
        GBAN_LOG_GROUP = int(GBAN_LOG_GROUP)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    ANDENCENTO_HNDLR = os.environ.get("ANDENCENTO_HNDLR", ".")
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    GROUP_REG_SED_EX_BOT_S = os.environ.get("GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)Andencento")
    HANDLER = os.environ.get("HANDLER", r"\.")
    HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    INSTANT_BLOCK = os.environ.get("INSTANT_BLOCK", "DISABLE")
    LOCATION = os.environ.get("LOCATION", None)
    LOGGER_ID = os.environ.get("LOGGER_ID", None)
    if LOGGER_ID:
        LOGGER_ID = int(LOGGER_ID)
    LYDIA_API = os.environ.get("LYDIA_API", None)
    MAX_ANTI_FLOOD_MESSAGES = 10
    MAX_MESSAGE_SIZE_LIMIT = 4095
    MAX_SPAM = int(os.environ.get("MAX_SPAM", 3))
    MONGO_URI = os.environ.get("MONGO_URI", None)
    MY_CHANNEL = os.environ.get("YOUR_CHANNEL", "Andencento")
    MY_GROUP = os.environ.get("YOUR_GROUP", "AndencentoSupport")
    OCR_API = os.environ.get("OCR_API", None)
    PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", None)
    if PLUGIN_CHANNEL:
        PLUGIN_CHANNEL = int(PLUGIN_CHANNEL)
    PM_LOG_ID = os.environ.get("PM_LOG_ID", None)
    if PM_LOG_ID:
        PM_LOG_ID = int(PM_LOG_ID)
    PM_PERMIT = os.environ.get("PM_PERMIT", "ENABLE")
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
    REMOVE_BG_API = os.environ.get("REMOVE_BG_API", None)
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    STICKER_PACKNAME = os.environ.get("STICKER_PACKNAME", None)
    SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"\.")
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    TAG_LOGGER = os.environ.get("TAG_LOGGER", None)
    if TAG_LOGGER: 
        TAG_LOGGER = int(TAG_LOGGER)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "AndencentoBot")
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    TZ = os.environ.get("TZ", "Asia/Kolkata")
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/Team-Andencento/Andencento")
    WEATHER_API = os.environ.get("WEATHER_API", None)
    YOUR_NAME = os.environ.get("YOUR_NAME", None)
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)    
   
