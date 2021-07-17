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
TEXT = "`Currently I am Working Fine my peru master!` **Andencento Userbot**\n\n"
                     "`Telethon version: 1.23.0\nPython: 3.9.6\n`"
                     "`Bot created by:` [Noob-Stranger](tg://user?id=1725374070), @NoobStrangerPerson\n"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "https://github.com/Noob-Stranger/andencento"
async def up(op):
    if op.fwd_from:
        return
    await op.get_chat()
    await op.delete()
    await borg.send_file(op.chat_id, PIC, caption=TEXT)
    await op.delete() 
