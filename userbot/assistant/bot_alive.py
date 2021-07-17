from telethon import events
from .. import ver
import os
from userbot import YOUR_NAME as ALIVE_NAME, bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.23.0` \n"
pm_caption += "➥ **Python:** `3.9.6` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `{ver}`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += f"➥ **License** : [GNU Affero General Public License v3.0](https://github.com/Noob-Stranger/andencento/blob/master/LICENSE)\n"
pm_caption += (
    "➥ **Copyright** : By [Andencento](https://github.com/Noob-Stranger/andencento)\n"
)
pm_caption += "[Assistant By Andencento](https://t.me/AndencentoSupport)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
