import asyncio
import os
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
PIC = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Andencento User"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PIC, "`Currently Alive, my peru master!` **Andencento Userbot**\n\n"
                     "`Telethon version: 1.23.0\nPython: 3.9.6\n`"
                     "`Bot created by:` [Noob-Stranger](tg://user?id=1725374070), @NoobStrangerPerson\n"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "https://github.com/Noob-Stranger/andencento")
