import asyncio
import json
import math
import os
import subprocess
import time
import datetime
import requests

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo

from . import *

@Andencento.on(admin_cmd(pattern=r"webup ?(.*)", outgoing=True))
@Andencento.on(sudo_cmd(pattern=r"webup ?(.*)", allow_sudo=True))
async def labstack(event):
    if event.fwd_from:
        return
    await eor(event, "Processing...")
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if input_str:
        filebase = input_str
    elif reply:
        filebase = await event.client.download_media(
            reply.media, Config.TMP_DOWNLOAD_DIRECTORY
        )
    else:
        await eod(event, "Reply to a media file or provide a directory to upload the file to labstack"
        )
        return
    filesize = os.path.getsize(filebase)
    filename = os.path.basename(filebase)
    headers2 = {"Up-User-ID": "IZfFbjUcgoo3Ao3m"}
    files2 = {
        "ttl": 604800,
        "files": [{"name": filename, "type": "", "size": filesize}],
    }
    r2 = requests.post(
        "https://up.labstack.com/api/v1/links", json=files2, headers=headers2
    )
    r2json = json.loads(r2.text)

    url = "https://up.labstack.com/api/v1/links/{}/send".format(r2json["code"])
    max_days = 7
    command_to_exec = [
        "curl",
        "-F",
        "files=@" + filebase,
        "-H",
        "Transfer-Encoding: chunked",
        "-H",
        "Up-User-ID: IZfFbjUcgoo3Ao3m",
        url,
    ]
    try:
        logger.info(command_to_exec)
        t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        logger.info("Status : FAIL", exc.returncode, exc.output)
        await eor(event, exc.output.decode("UTF-8"))
        return
    else:
        logger.info(t_response)
        t_response_arry = "https://up.labstack.com/api/v1/links/{}/receive".format(
            r2json["code"]
        )
    await eor(event, t_response_arry + "\nMax Days:" + str(max_days), link_preview=False
    )


@Andencento.on(admin_cmd(pattern=r"upld_dir (.*)", outgoing=True))
@Andencento.on(sudo_cmd(pattern=r"upld_dir (.*)", allow_sudo=True))
async def uploadir(udir_event):
    """ For .uploadir command, allows you to upload everything from a folder in the server"""
    input_str = udir_event.pattern_match.group(1)
    if os.path.exists(input_str):
        await udir_event.edit("Downloading Using Userbot Server....")
        lst_of_files = []
        for r, d, f in os.walk(input_str):
            for file in f:
                lst_of_files.append(os.path.join(r, file))
            for file in d:
                lst_of_files.append(os.path.join(r, file))
        LOGS.info(lst_of_files)
        uploaded = 0
        await udir_event.edit(
            "Found {} files. Uploading will start soon. Please wait!".format(
                len(lst_of_files)
            )
        )
        for single_file in lst_of_files:
            if os.path.exists(single_file):
                # https://stackoverflow.com/a/678242/4723940
                caption_rts = os.path.basename(single_file)
                c_time = time.time()
                if not caption_rts.lower().endswith(".mp4"):
                    await udir_event.client.send_file(
                        udir_event.chat_id,
                        single_file,
                        caption=caption_rts,
                        force_document=False,
                        allow_cache=False,
                        reply_to=udir_event.message.id,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d,
                                t,
                                udir_event,
                                c_time,
                                "Uploading in Progress.......",
                                single_file,
                            )
                        ),
                    )
                else:
                    thumb_image = os.path.join(input_str, "thumb.jpg")
                    c_time = time.time()
                    metadata = extractMetadata(createParser(single_file))
                    duration = 0
                    width = 0
                    height = 0
                    if metadata.has("duration"):
                        duration = metadata.get("duration").seconds
                    if metadata.has("width"):
                        width = metadata.get("width")
                    if metadata.has("height"):
                        height = metadata.get("height")
                    await udir_event.client.send_file(
                        udir_event.chat_id,
                        single_file,
                        caption=caption_rts,
                        thumb=thumb_image,
                        force_document=False,
                        allow_cache=False,
                        reply_to=udir_event.message.id,
                        attributes=[
                            DocumentAttributeVideo(
                                duration=duration,
                                w=width,
                                h=height,
                                round_message=False,
                                supports_streaming=True,
                            )
                        ],
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d, t, udir_event, c_time, "Uploading...", single_file
                            )
                        ),
                    )
                os.remove(single_file)
                uploaded = uploaded + 1
        await udir_event.delete()
        await udir_event.edit("Uploaded {} files successfully !!".format(uploaded))
    else:
        await udir_event.edit("404: Directory Not Found")


import asyncio
import io
import os
import pathlib
import subprocess
import time
from datetime import datetime
from pathlib import Path

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl import types
from telethon.utils import get_attributes

from userbot import Andencento

from ..config import Config
from ..utils import edit_delete, edit_or_reply
from ..helpers import progress


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id



PATH = os.path.join("userbot/cache", "temp_vid.mp4")
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
downloads = pathlib.Path("userbot/cach").absolute()
NAME = "untitled"


class UPLOAD:
    def __init__(self):
        self.uploaded = 0


UPLOAD_ = UPLOAD()


async def catlst_of_files(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all filenames.
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
    return files


def get_video_thumb(file, output=None, width=320):
    output = file + ".jpg"
    metadata = extractMetadata(createParser(file))
    cmd = [
        "ffmpeg",
        "-i",
        file,
        "-ss",
        str(int((0, metadata.get("duration").seconds)[metadata.has("duration")] / 2)),
        # '-filter:v', 'scale={}:-1'.format(width),
        "-vframes",
        "1",
        output,
    ]
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    p.communicate()
    if not p.returncode and os.path.lexists(file):
        return output


def sortthings(contents, path):
    catsort = []
    contents.sort()
    for file in contents:
        catpath = os.path.join(path, file)
        if os.path.isfile(catpath):
            catsort.append(file)
    for file in contents:
        catpath = os.path.join(path, file)
        if os.path.isdir(catpath):
            catsort.append(file)
    return catsort


async def _get_file_name(path: pathlib.Path, full: bool = True) -> str:
    return str(path.absolute()) if full else path.stem + path.suffix


async def upload(path, event, udir_event, catflag=None):  # sourcery no-metrics
    catflag = catflag or False
    reply_to_id = await reply_id(event)
    if os.path.isdir(path):
        await event.client.send_message(
            event.chat_id,
            f"**Folder : **`{str(path)}`",
        )
        Files = os.listdir(path)
        Files = sortthings(Files, path)
        for file in Files:
            catpath = os.path.join(path, file)
            await upload(Path(catpath), event, udir_event)
    elif os.path.isfile(path):
        fname = os.path.basename(path)
        c_time = time.time()
        thumb = None
        if os.path.exists(thumb_image_path):
            thumb = thumb_image_path
        f = path.absolute()
        attributes, mime_type = get_attributes(str(f))
        ul = io.open(f, "rb")
        uploaded = await event.client.fast_upload_file(
            file=ul,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "trying to upload", file_name=fname)
            ),
        )
        ul.close()
        media = types.InputMediaUploadedDocument(
            file=uploaded,
            mime_type=mime_type,
            attributes=attributes,
            force_file=catflag,
            thumb=await event.client.upload_file(thumb) if thumb else None,
        )
        await event.client.send_file(
            event.chat_id,
            file=media,
            caption=f"**File Name : **`{fname}`",
            reply_to=reply_to_id,
        )

        UPLOAD_.uploaded += 1


@Andencento.on(admin_cmd(pattern=r"upload (.*)", outgoing=True))
async def uploadir(event):
    "To upload files to telegram."
    input_str = event.pattern_match.group(2)
    path = Path(input_str)
    start = datetime.now()
    flag = event.pattern_match.group(1)
    flag = bool(flag)
    if not os.path.exists(path):
        return await edit_or_reply(
            event,
            f"`there is no such directory/file with the name {path} to upload`",
        )
    udir_event = await edit_or_reply(event, "Uploading....")
    if os.path.isdir(path):
        await edit_or_reply(udir_event, f"`Gathering file details in directory {path}`")
        UPLOAD_.uploaded = 0
        await upload(path, event, udir_event, catflag=flag)
        end = datetime.now()
        ms = (end - start).seconds
        await edit_delete(
            udir_event,
            f"`Uploaded {UPLOAD_.uploaded} files successfully in {ms} seconds. `",
        )
    else:
        await edit_or_reply(udir_event, f"`Uploading file .....`")
        UPLOAD_.uploaded = 0
        await upload(path, event, udir_event, catflag=flag)
        end = datetime.now()
        ms = (end - start).seconds
        await edit_delete(
            udir_event, f"`Uploaded file {str(path)} successfully in {ms} seconds. `"
        )


@Andencento.on(admin_cmd(pattern=r"upld_as(stream|vn|all) (.*)", outgoing=True))
@Andencento.on(sudo_cmd(pattern=r"upld_as (stream|vn|all) (.*)", allow_sudo=True))
async def uploadas(uas_event):
    """ For .uploadas command, allows you to specify some arguments for upload. """
    await uas_event.edit("Processing ...")
    type_of_upload = uas_event.pattern_match.group(1)
    supports_streaming = False
    round_message = False
    spam_big_messages = False
    if type_of_upload == "stream":
        supports_streaming = True
    if type_of_upload == "vn":
        round_message = True
    if type_of_upload == "all":
        spam_big_messages = True
    input_str = uas_event.pattern_match.group(2)
    thumb = None
    file_name = None
    if "|" in input_str:
        file_name, thumb = input_str.split("|")
        file_name = file_name.strip()
        thumb = thumb.strip()
    else:
        file_name = input_str
        thumb_path = "a_random_f_file_name" + ".jpg"
        thumb = get_video_thumb(file_name, output=thumb_path)
    if os.path.exists(file_name):
        metadata = extractMetadata(createParser(file_name))
        duration = 0
        width = 0
        height = 0
        if metadata.has("duration"):
            duration = metadata.get("duration").seconds
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        try:
            if supports_streaming:
                c_time = time.time()
                await uas_event.client.send_file(
                    uas_event.chat_id,
                    file_name,
                    thumb=thumb,
                    caption=input_str,
                    force_document=False,
                    allow_cache=False,
                    reply_to=uas_event.message.id,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=duration,
                            w=width,
                            h=height,
                            round_message=False,
                            supports_streaming=True,
                        )
                    ],
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, uas_event, c_time, "Uploading...", file_name)
                    ),
                )
            elif round_message:
                c_time = time.time()
                await uas_event.client.send_file(
                    uas_event.chat_id,
                    file_name,
                    thumb=thumb,
                    allow_cache=False,
                    reply_to=uas_event.message.id,
                    video_note=True,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=0,
                            w=1,
                            h=1,
                            round_message=True,
                            supports_streaming=True,
                        )
                    ],
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, uas_event, c_time, "Uploading...", file_name)
                    ),
                )
            elif spam_big_messages:
                await uas_event.edit("TBD: Not (yet) Implemented")
                return
            os.remove(thumb)
            await uas_event.edit("Uploaded successfully !!")
        except FileNotFoundError as err:
            await uas_event.edit(str(err))
    else:
        await uas_event.edit("404: File Not Found")


import asyncio
import io
import math
import os
import pathlib
import time
from datetime import datetime

from pySmartDL import SmartDL
from telethon.tl import types
from telethon.utils import get_extension

from userbot import catub

from ..config import Config
from ..utils import edit_delete, edit_or_reply
from ..helpers import humanbytes, progress
from ..helpers.utils import _format

plugin_category = "misc"

NAME = "untitled"

downloads = pathlib.Path(os.path.join(os.getcwd(), Config.TMP_DOWNLOAD_DIRECTORY))


async def _get_file_name(path: pathlib.Path, full: bool = True) -> str:
    return str(path.absolute()) if full else path.stem + path.suffix


@Andencento.on(admin_cmd(pattern="download(?: |$)(.*)", outgoing=True))
async def _(event):  # sourcery no-metrics
    "To download the replied telegram file"
    mone = await edit_or_reply(event, "`Downloading....`")
    input_str = event.pattern_match.group(3)
    name = NAME
    path = None
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    reply = await event.get_reply_message()
    if reply:
        start = datetime.now()
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        if input_str:
            path = pathlib.Path(os.path.join(downloads, input_str.strip()))
        else:
            path = pathlib.Path(os.path.join(downloads, name))
        ext = get_extension(reply.document)
        if path and not path.suffix and ext:
            path = path.with_suffix(ext)
        if name == NAME:
            name += "_" + str(getattr(reply.document, "id", reply.id)) + ext
        if path and path.exists():
            if path.is_file():
                newname = str(path.stem) + "_OLD"
                path.rename(path.with_name(newname).with_suffix(path.suffix))
                file_name = path
            else:
                file_name = path / name
        elif path and not path.suffix and ext:
            file_name = downloads / path.with_suffix(ext)
        elif path:
            file_name = path
        else:
            file_name = downloads / name
        file_name.parent.mkdir(parents=True, exist_ok=True)
        c_time = time.time()
        if (
            not reply.document
            and reply.photo
            and file_name
            and file_name.suffix
            or not reply.document
            and not reply.photo
        ):
            await reply.download_media(
                file=file_name.absolute(),
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
        elif not reply.document:
            file_name = await reply.download_media(
                file=downloads,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
        else:
            dl = io.FileIO(file_name.absolute(), "a")
            await event.client.fast_download_file(
                location=reply.document,
                out=dl,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
            dl.close()
        end = datetime.now()
        ms = (end - start).seconds
        await mone.edit(
            f"**•  Downloaded in {ms} seconds.**\n**•  Downloaded to :- **  `{os.path.relpath(file_name,os.getcwd())}`\n   "
        )
    elif input_str:
        start = datetime.now()
        if "|" in input_str:
            url, file_name = input_str.split("|")
        else:
            url = input_str
            file_name = None
        url = url.strip()
        file_name = os.path.basename(url) if file_name is None else file_name.strip()
        downloaded_file_name = pathlib.Path(os.path.join(downloads, file_name))
        if not downloaded_file_name.suffix:
            ext = os.path.splitext(url)[1]
            downloaded_file_name = downloaded_file_name.with_suffix(ext)
        downloader = SmartDL(url, str(downloaded_file_name), progress_bar=False)
        downloader.start(blocking=False)
        c_time = time.time()
        count = 0
        oldmsg = ""
        while not downloader.isFinished():
            total_length = downloader.filesize or None
            downloaded = downloader.get_dl_size()
            now = time.time()
            now - c_time
            percentage = downloader.get_progress() * 100
            downloader.get_speed()
            progress_str = "`{0}{1} {2}`%".format(
                "".join("▰" for i in range(math.floor(percentage / 5))),
                "".join("▱" for i in range(20 - math.floor(percentage / 5))),
                round(percentage, 2),
            )
            estimated_total_time = downloader.get_eta(human=True)
            current_message = f"Downloading the file\
                                \n\n**URL : **`{url}`\
                                \n**File Name :** `{file_name}`\
                                \n{progress_str}\
                                \n`{humanbytes(downloaded)} of {humanbytes(total_length)}`\
                                \n**ETA : **`{estimated_total_time}`"
            count += 1
            if oldmsg != current_message:
                if count >= 0.5:
                    count = 0
                    await mone.edit(current_message)
                oldmsg = current_message
            await asyncio.sleep(1)
        end = datetime.now()
        ms = (end - start).seconds
        if downloader.isSuccessful():
            await mone.edit(
                f"**•  Downloaded in {ms} seconds.**\n**•  Downloaded file location :- ** `{os.path.relpath(downloaded_file_name,os.getcwd())}`"
            )
        else:
            await mone.edit("Incorrect URL\n {}".format(input_str))
    else:
        await mone.edit("`Reply to a message to download to my local server.`")


@Andencento.on(admin_cmd(pattern="dlto(?: |$)(.*)", outgoing=True))
async def _(event):  # sourcery no-metrics
    pwd = os.getcwd()
    input_str = event.pattern_match.group(3)
    if not input_str:
        return await edit_delete(
            event,
            "Where should i save this file. mention folder name",
            parse_mode=_format.parse_pre,
        )

    location = os.path.join(pwd, input_str)
    if not os.path.isdir(location):
        os.makedirs(location)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event,
            "Reply to media file to download it to bot server",
            parse_mode=_format.parse_pre,
        )
    mone = await edit_or_reply(
        event, "Downloading the file ...", parse_mode=_format.parse_pre
    )
    start = datetime.now()
    for attr in getattr(reply.document, "attributes", []):
        if isinstance(attr, types.DocumentAttributeFilename):
            name = attr.file_name
    if input_str:
        path = pathlib.Path(os.path.join(location, input_str.strip()))
    else:
        path = pathlib.Path(os.path.join(location, name))
    ext = get_extension(reply.document)
    if path and not path.suffix and ext:
        path = path.with_suffix(ext)
    if name == NAME:
        name += "_" + str(getattr(reply.document, "id", reply.id)) + ext
    if path and path.exists():
        if path.is_file():
            newname = str(path.stem) + "_OLD"
            path.rename(path.with_name(newname).with_suffix(path.suffix))
            file_name = path
        else:
            file_name = path / name
    elif path and not path.suffix and ext:
        file_name = location / path.with_suffix(ext)
    elif path:
        file_name = path
    else:
        file_name = location / name
    file_name.parent.mkdir(parents=True, exist_ok=True)
    c_time = time.time()
    if (
        not reply.document
        and reply.photo
        and file_name
        and file_name.suffix
        or not reply.document
        and not reply.photo
    ):
        await reply.download_media(
            file=file_name.absolute(),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, mone, c_time, "trying to download")
            ),
        )
    elif not reply.document:
        file_name = await reply.download_media(
            file=location,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, mone, c_time, "trying to download")
            ),
        )
    else:
        dl = io.FileIO(file_name.absolute(), "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, mone, c_time, "trying to download")
            ),
        )
        dl.close()
    end = datetime.now()
    ms = (end - start).seconds
    await mone.edit(
        f"**•  Downloaded in {ms} seconds.**\n**•  Downloaded to :- **  `{os.path.relpath(file_name,os.getcwd())}`\n   "
    )


CmdHelp("up_down").add_command(
  "upload", "<path>", "Uploads a locally stored file to the chat"
).add_command(
  "dlto", "<path>", "Uploads a locally stored file to the chat"
).add_command(
  "upld_as stream", "<path>", "Uploads the locally stored file in streamable format"
).add_command(
  "upld_as vn", "<path>", "Uploads the locally stored file in vs format"
).add_command(
  "upldir", "<path>", "Uploads all the files in directory"
).add_command(
  "download", "<link/filename> or reply to media", "Downloads the file to the server"
).add_command(
  "webup", "<reply to media>", "Makes a direct download link of the replied media for a limited time"
).add_info(
  "Upload & Download."
).add_warning(
  "✅ Harmless Module."
).add()
