import asyncio
import io
import os
import sys
import traceback
from .. import *
from ..config import Config
from telethon import events

I_AM_DEVELOPER = os.environ.get("I_AM_DEVELOPER", None)

@tgbot.on(events.NewMessage(pattern="/eval ?(.*)"))
async def _(event):
  if I_AM_DEVELOPER != "True":
    await tgbot.send_message(
      event,
      f"Developer Restricted!\nIf you know what this does, and want to proceed\n\n {HANDLER}set var I_AM_DEVELOPER True\n\nThis Might Be Dangerous.",
      )
    return
    pro = await bot.get_me()
    boy = pro.id
    if event.sender_id == boy or event.sender_id == id or event.sender_id == id:
       pass
    else:
       return await event.reply("deploy your own Bot ")
    cmd = event.text.split(" ", maxsplit=1)[1]
    if not cmd:
        return await event.reply("What should I run ?..\n\nGive me something to run, u dumbo!!")
    proevent = await event.reply("Running.....")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Sᴜᴄᴄᴇss ✅"
    final_output = f"**•  Eᴠᴀʟ : **\n`{cmd}` \n\n**•  Rᴇsᴜʟᴛ : **\n`{evaluation}` \n"
    await proevent.edit(final_output)


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, event , reply, client, p, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )




@tgbot.on(events.NewMessage(pattern="/exec ?(.*)"))
async def _(event):
  if I_AM_DEVELOPER != "True":
    await tgbot.send_message(
      event,
      f"Developer Restricted!\nIf you know what this does, and want to proceed\n\n {HANDLER}set var I_AM_DEVELOPER True\n\nThis Might Be Dangerous.",
      )
    return
    pro = await bot.get_me()
    boy = pro.id
    if event.sender_id == boy or event.sender_id == id:
       pass
    else:
       return await event.reply("deploy your Bot")
    cmd = event.text.split(" ", maxsplit=1)[1]
    if not cmd:
        return await event.reply("What should I execute?..\n\nGive me somwthing to execute, u dumbo!!")
    proevent = await event.reply("Executing.....")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    curruser = pro.username or "Ultra.on"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"`{curruser}:~#` `{cmd}`\n`{result}`"
    else:
        cresult = f"`{curruser}:~$` `{cmd}`\n`{result}`"
    await proevent.edit(cresult)
