from pydantic import BaseModel
from typing import Any


class IdentifyDataToken(BaseModel):
    token: str
    properties = {
      "os": "linux",
      "browser": "disco",
      "device": "disco"
    }
    compress = False
    intents: int


class IdentifyData(BaseModel):
    op = 2
    d: IdentifyDataToken


class Config(BaseModel):
    wss_url: str
    bot_token: str
    identify_data: IdentifyData


class InitMessageData(BaseModel):
    heartbeat_interval: int
    _trace: list[Any]


class InitMessage(BaseModel):
    t: Any|None
    s: Any|None
    op: int
    d: InitMessageData


class IdentifyMessageData(BaseModel):
    user_settings: dict
    session_type: str
    session_id: str
    resume_gateway_url: str


class IdentifyMessage(BaseModel):
    t: str|None
    s: int|None
    op: int|None
    d: IdentifyMessageData

