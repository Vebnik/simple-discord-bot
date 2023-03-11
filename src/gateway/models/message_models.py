from datetime import datetime
from typing import Any
from pydantic import BaseModel

from src.api.api import interface, API
# from src.discord.app import App


class Author(BaseModel):
    username: str
    public_flags: int
    id: int
    display_name: Any|str
    discriminator: int
    avatar_decoration: Any|None
    avatar: str|None


class Member(BaseModel):
    roles: list[int]
    premium_since: Any|None
    pending: bool
    nick: Any|None
    mute: bool
    joined_at: datetime
    flags: int
    deaf: bool
    communication_disabled_until: Any|None
    avatar: Any|None


class MessageEvent(BaseModel):
    type: int|None
    tts: bool|None
    timestamp: datetime|None
    referenced_message: Any|None
    pinned: bool|None
    nonce: int|None
    mentions: list[Any]|None
    mention_roles: list[Any]|None
    mention_everyone: bool|None
    member: Member|None
    id: int
    flags: int|None
    embeds: list[Any]|None
    edited_timestamp: Any|None
    content: str|None
    components: list[Any]|None
    channel_id: int
    author: Author|None
    attachments: list[Any]|None
    guild_id: int
    app: Any|None

    def reply(self, content: str, embeds = []) -> None:
        api: API = interface['api']
        api.create_ref_message(self.channel_id, self.id, self.guild_id, content, embeds)