import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from . import LOGS, Andencento, tbot
from config import Config
from .utils import load_module
