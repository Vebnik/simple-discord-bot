from datetime import datetime
from typing import Any
from pydantic import BaseModel


class User(BaseModel):
    verified: bool
    username: str
    mfa_enabled: bool
    id: str
    flags: int
    email: str|None
    display_name: str|None
    discriminator: int
    bot: bool
    avatar: str|None


class ReadyEvent(BaseModel):
    v: int
    user_settings: Any|None
    user: User
    session_type: str
    session_id: str
    resume_gateway_url: str
    relationships: list[Any]
    private_channels: list[Any]
    presences: list[Any]
    guilds: list[dict|None]|None
    guild_join_requests: list[Any]
    geo_ordered_rtc_regions: list[str]
    application: dict[str, Any]