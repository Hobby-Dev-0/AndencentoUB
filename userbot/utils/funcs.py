
from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import (ChannelParticipantAdmin,
                               ChannelParticipantCreator)

from .. import *
from ..helpers import *


# just a small shit for big works
class Loader:
    def __init__(self, func=None, **args):
        self.Var = Var
        Andencento.add_event_handler(func, events.NewMessage(**args))


# Check if Admin
async def is_admin(client, chat_id, user_id):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        errorshivansh = await client(GetParticipantRequest(channel=chat_id, user_id=user_id))
        chat_participant = errorshivansh.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception:
        return False
    else:
        return False
# 
