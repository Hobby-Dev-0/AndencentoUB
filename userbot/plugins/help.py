
import asyncio
import requests
from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

Eiva_channel = "@Andencento"

msg = f"""
**⚡ ᴜʟᴛɪᴍᴀᴛᴇ ᴜꜱᴇʀʙᴏᴛ ᴀɴᴅᴇɴᴄᴇɴᴛᴏ⚡**
  •        [📑 Repo 📑](https://github.com/Team-Andencento/Andencento)
  •        [🚀 Deploy 🚀](https://github.com/Team-Andencento/Andencento)
  •  ©️ {Eiva_channel} ™
"""
botname = Config.BOT_USERNAME

@Andencento.on(admin_cmd(pattern="repo$"))
@Andencento.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def repo(event):
    try:
        Eiva = await bot.inline_query(botname, "repo")
        await Eiva[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@Andencento.on(admin_cmd(pattern="shelp ?(.*)", outgoing=True))
@Andencento.on(sudo_cmd(pattern="shelp ?(.*)", allow_sudo=True))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = Config.BOT_USERNAME
    input_str = event.pattern_match.group(1)
    try:
        if not input_str == "":
            if input_str in CMD_HELP:
                await eor(event, str(CMD_HELP[args]))
    except:
        pass
    if tgbotusername is not None:
        results = await event.client.inline_query(tgbotusername, "Eivabot_help")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await eor(event, "**⚠️ ERROR !!** \nPlease Re-Check BOT_TOKEN & BOT_USERNAME on Heroku.")


@Andencento.on(admin_cmd(pattern="plinfo(?: |$)(.*)", outgoing=True))
@Andencento.on(sudo_cmd(pattern="plinfo(?: |$)(.*)", allow_sudo=True))
async def Eivabott(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eod(event, "**⚠️ Error !** \nNeed a module name to show plugin info.")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`▶️ `"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eod(event, "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string)
