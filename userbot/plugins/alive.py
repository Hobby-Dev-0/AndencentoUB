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
YOUR_NAME = os.environ.get("YOUR_NAME")
from telethon.tl.types import ChannelParticipantsAdmins


DEFAULTUSER = str(YOUR_NAME) if YOUR_NAME else "ᴀɴᴅᴇɴᴄᴇɴᴛᴏ ᴜꜱᴇʀ"
""" =======================CONSTANTS====================== """
EXTREMEPRO_PIC = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
EXTREMEPRO = f"**`Owner`: {DEFAULTUSER}`**\n\n"
EXTREMEPRO = f" ┏━━━━━━━━━━━━━━━━━━━\n"
EXTREMEPRO = f" ┣•➳➠ **`Owner`: {DEFAULTUSER}`**\n\n"
EXTREMEPRO += f"┣•➳➠ ""ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ "":"" `1.21.1` \n"
EXTREMEPRO += f"┣•➳➠ ""ᴀɴᴅᴇɴᴄᴇɴᴛᴏ ᴠᴇʀꜱɪᴏɴ "":"" `0.0.2'`\n"
EXTREMEPRO += f"┣•➳➠ ""ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ "":"" `3.9.6`\n"
EXTREMEPRO += f"┣•➳➠ ""ꜱᴜᴘᴘᴏʀᴛ "":"" [𝔖𝔲𝔭𝔭𝔬𝔯𝔱](https://t.me/Andencentosupport)\n"
EXTREMEPRO += f"┣•➳➠ ""яєρσ🔥 "":"" [яєρσ🔥](https://github.com/Noob-Stranger/andencento)\n"
EXTREMEPRO += f"┣•➳➠ ""ɖɛքʟօʏ⚡"" :"" [ɖɛքʟօʏ⚡Me](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FNoob-Stranger%2Fandencentopack&template=https%3A%2F%2Fgithub.com%2FNoob-Stranger%2Fandencentopack)\n"
EXTREMEPRO += f"┣•➳➠ ""ᴀɴᴅᴇɴᴄᴇɴᴛᴏ ꜱᴇꜱꜱɪᴏɴ"" :"" [ᴀɴᴅᴇɴᴄᴇɴᴛᴏ ꜱᴇꜱꜱɪᴏɴ](https://replit.com/@amanpandey7647/ANDENCENTOSESSION)\n"
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
