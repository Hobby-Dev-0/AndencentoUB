import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc

from telethon import events

import time
import datetime
from .. import StartTime
def upt():
   uptm = get_readable_time((time.time() - StartTime))
