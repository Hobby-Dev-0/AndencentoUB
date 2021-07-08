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
from ..config import *
from ..utils import *
from var import Var


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from userAndencento.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import userAndencento.utils

        path = Path(f"userAndencento/plugins/{shortname}.py")
        name = "userAndencento.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:
        import userAndencento.utils

        path = Path(f"userAndencento/plugins/{shortname}.py")
        name = "userAndencento.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.Andencento = Andencento
        mod.admin_cmd = Andencento
        mod.Var = Var
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        mod.LOGS = LOGS
        mod.tgAndencento = Andencento.tgAndencento
        mod.sudo_cmd = sudo_cmd
        sys.modules["userAndencento"] = userAndencento
        sys.modules["userAndencento.utils"] = userAndencento.utils
        sys.modules["Extre.events"] = userAndencento.utils
        sys.modules["userAndencento.events"] = userAndencento.utils
        sys.modules["ULTRA.utils"] = userAndencento.utils
        sys.modules["userAndencento.Config"] = userAndencento.config
        sys.modules["userAndencento.uniborConfig"] = userAndencento.config
        sys.modules["ub"] = userAndencento
        sys.modules["var"] = userAndencento.var
        sys.modules["jarvis"] = userAndencento
        sys.modules["support"] = userAndencento
        sys.modules["userAndencento"] = userAndencento
        sys.modules["teleAndencento"] = userAndencento
        sys.modules["fridayAndencento"] = userAndencento
        sys.modules["jarvis.utils"] = userAndencento.utils
        sys.modules["uniborg.util"] = userAndencento.utils
        sys.modules["teleAndencento.utils"] = userAndencento.utils
        sys.modules["userAndencento.utils"] = userAndencento.utils
        sys.modules["userAndencento.events"] = userAndencento.utils
        sys.modules["jarvis.jconfig"] = userAndencento.config
        sys.modules["userAndencento.config"] = userAndencento.config
        sys.modules["fridayAndencento.utils"] = userAndencento.utils
        sys.modules["fridayAndencento.Config"] = userAndencento.config
        sys.modules["userAndencento.uniborgConfig"] = userAndencento.config
        mod.edit_or_reply = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = userAndencento.utils
        mod.Config = Config
        mod.borg = Andencento
        mod.edit_or_reply = edit_or_reply
        # support for paperplaneextended
        sys.modules["userAndencento.mainfiles.events"] = userAndencento.utils
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["userAndencento.plugins." + shortname] = mod
        LOGS.info("Andencento imported " + shortname)

def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                Andencento.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"plugins.{shortname}"

            for i in reversed(range(len(Andencento._event_builders))):
                ev, cb = Andencento._event_builders[i]
                if cb.__module__ == name:
                    del Andencento._event_builders[i]
    except BaseException:
        raise ValueError
