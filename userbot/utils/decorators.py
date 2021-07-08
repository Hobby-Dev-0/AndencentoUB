import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from .. import *
from ..helpers import *
from ..config import Config
from ..sql import sudo_sql as s_ql

# admin cmd or normal user cmd
def admin_cmd(pattern=None, command=None, **args):
    args["func"] = lambda e: e.via_Andencento_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith(r"\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        else:
            if len(Config.ANDENCENTO_HNDLR) == 2:
                Andencentoreg = "^" + Config.ANDENCENTO_HNDLR
                reg = Config.ANDENCENTO_HNDLR[1]
            elif len(Config.ANDENCENTO_HNDLR) == 1:
                Andencentoreg = "^\\" + Config.ANDENCENTO_HNDLR
                reg = Config.ANDENCENTO_HNDLR
            args["pattern"] = re.compile(Andencentoreg + pattern)
            if command is not None:
                cmd = reg + command
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # decides that other users can use it or not
    # Andencento outgoing
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # blacklisted chats. 
    # Andencento will not respond in these chats.
    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if black_list_chats:
        args["chats"] = black_list_chats

    # blacklisted chats.
    # AndencentoAndencento will not respond in these chats.
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]

    # plugin check for outgoing commands

    return events.NewMessage(**args)


def sudo_cmd(pattern=None, command=None, **args):
    args["func"] = lambda e: e.via_Andencento_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith(r"\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                SUDO_LIST[file_test].append(cmd)
            except BaseException:
                SUDO_LIST.update({file_test: [cmd]})
        else:
            if len(Config.SUDO_HANDLER) == 2:
                Andencentoreg = "^" + Config.SUDO_HANDLER
                reg = Config.SUDO_HANDLER[1]
            elif len(Config.SUDO_HANDLER) == 1:
                Andencentoreg = "^\\" + Config.SUDO_HANDLER
                reg = Config.HANDLER
            args["pattern"] = re.compile(Eivareg + pattern)
            if command is not None:
                cmd = reg + command
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                SUDO_LIST[file_test].append(cmd)
            except BaseException:
                SUDO_LIST.update({file_test: [cmd]})
    args["outgoing"] = True
    # outgoing check
    # AndencentoAndencento
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]
    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True
    # blacklisted chats
    # Andencento won't respond here
    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if black_list_chats:
        args["chats"] = black_list_chats
    # blacklisted chats
    # AndencentoAndencento won't respond here
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]
    # outgoing check
    # Andencento
    return events.NewMessage(**args)

# Configration of Andencento cmd
on = Andencento.on


def on(**args):
    def decorator(func):
        async def wrapper(event):
            # check if sudo
            await func(event)

        client.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorater


# register decorate
def register(**args):
    args["func"] = lambda e: e.via_Andencento_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    disable_edited = args.get("disable_edited", True)
    allow_sudo = args.get("allow_sudo", False)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass

            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        except BaseException:
            pass

    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    def decorator(func):
        if not disable_edited:
            Andencento.add_event_handler(func, events.MessageEdited(**args))
        Andencento.add_event_handler(func, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


# command decorations
def command(**args):
    args["func"] = lambda e: e.via_Andencento_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    pattern = args.get("pattern", None)
    allow_sudo = args.get("allow_sudo", None)
    allow_edited_updates = args.get("allow_edited_updates", False)
    args["incoming"] = args.get("incoming", False)
    args["outgoing"] = True
    if bool(args["incoming"]):
        args["outgoing"] = False

    try:
        if pattern is not None and not pattern.startswith("(?i)"):
            args["pattern"] = "(?i)" + pattern
    except BaseException:
        pass

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        except BaseException:
            pass
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
    del allow_sudo
    try:
        del args["allow_sudo"]
    except BaseException:
        pass

    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if "allow_edited_updates" in args:
        del args["allow_edited_updates"]

    def decorator(func):
        if allow_edited_updates:
            Andencento.add_event_handler(func, events.MessageEdited(**args))
        Andencento.add_event_handler(func, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except BaseException:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator
