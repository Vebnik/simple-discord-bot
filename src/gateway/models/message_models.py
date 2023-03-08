from datetime import datetime
from typing import Any
from pydantic import BaseModel


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
    type: int
    tts: bool
    timestamp: datetime
    referenced_message: Any|None
    pinned: bool
    nonce: int
    mentions: list[Any]
    mention_roles: list[Any]
    mention_everyone: bool
    member: Member
    id: int
    flags: int
    embeds: list[Any]
    edited_timestamp: Any|None
    content: str
    components: list[Any]
    channel_id: int
    author: Author
    attachments: list[Any]
    guild_id: int

    async def reply(self, content: str) -> None:
        print(content)