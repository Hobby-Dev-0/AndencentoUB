# MADE BY PERRY_XD, AMAN PANDEY AND GODBOYX
# KANG WITH CREDITS 

"""
Syntax: .alive
"""


import asyncio
import os
import random
from telethon import events, TelegramClient
from . import *
from telethon.tl.types import ChannelParticipantsAdmins


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"
""" =======================CONSTANTS====================== """
EXTREMEPRO_PIC = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/d41fdd50ef5dd1359afcd.png"
EXTREMEPRO = f"**`Owner`: {DEFAULTUSER}`**\n\n"
EXTREMEPRO = f" ┏━━━━━━━━━━━━━━━━━━━\n"
EXTREMEPRO += f"┣•➳➠ `σωηєя :` `{DEFAULTUSER}` \n"
EXTREMEPRO += f"┣•➳➠ `ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :` `1.21.1` \n"
EXTREMEPRO += f"┣•➳➠ `ᴀɴᴅᴇɴᴄᴇɴᴛᴏ ᴠᴇʀꜱɪᴏɴ :` `0.0.1`\n"
EXTREMEPRO += f"┣•➳➠ `ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :` `3.9.5`\n"
EXTREMEPRO += f"┣•➳➠ `ꜱᴜᴘᴘᴏʀᴛ :` [𝔖𝔲𝔭𝔭𝔬𝔯𝔱](https://t.me/Andencentosupport)\n"
EXTREMEPRO += f"┣•➳➠ `υρтιмє :` `{StartTime}` \n"
EXTREMEPRO += f"┣•➳➠ `яєρσ🔥 :` [яєρσ🔥](https://github.com/Team-Andencento/Andencento)\n"
EXTREMEPRO += f"┣•➳➠ `ɖɛքʟօʏ⚡ :` [ɖɛքʟօʏ⚡Me](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeam-Andencento%2FAndencento-Deploy-Pack&template=https%3A%2F%2Fgithub.com%2FTeam-Andencento%2FAndencento-Deploy-Pack)\n"
EXTREMEPRO += f"┗━━━━━━━━━━━━━━━━━━━\n"
@Andencento.on(admin_cmd(outgoing=True, pattern="alive$"))
@Andencento.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(op):
    if op.fwd_from:
        return
    await op.get_chat()
    await op.delete()
    await borg.send_file(op.chat_id, EXTREMEPRO_PIC, caption=EXTREMEPRO)
    await op.delete() 
