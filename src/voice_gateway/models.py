from pydantic import BaseModel


class VoiceUpdateData(BaseModel):
    token: str
    guild_id: int
    endpoint: str


class VoiceUpdateEvent(BaseModel):
    t: str
    s: int
    op: int
    d: VoiceUpdateData


class VoiceIndentifyMessageData(BaseModel):
    ssrc: int
    port: int
    modes: list[str] = ['xsalsa20_poly1305_lite']
    ip: str
    experiments: list[str]


class VoiceIndentifyMessage(BaseModel):
    op: int
    d: VoiceIndentifyMessageData


class InitMessageData(BaseModel):
    v: int
    heartbeat_interval: int


class InitMessage(BaseModel):
    op: int
    d: InitMessageData


class SelectProtocolData(BaseModel):
    video_codec: str
    secret_key: list[int]
    mode: str
    media_session_id: str
    audio_codec: str


class SelectProtocolMessage(BaseModel):
    op: int
    d: SelectProtocolData