

from .. import *
from ..helpers import *


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"userbot/assistant/{shortname}.py")
        name = "userbot.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"userbot/assistant/{shortname}.py")
        name = "userbot.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = Andencento.tgbot
        spec.loader.exec_module(mod)
        sys.modules["assistant" + shortname] = mod
