from pydantic import BaseModel, validator


class ApiConfig(BaseModel):
    api_version: str
    base_url: str
    token: str

    @validator('api_version')
    def api_version_contains(cls, v: str):
        if 'v' not in v or len(v) < 2:
            raise ValueError('api version must contains "v" or have len >= 2')
        
        return v

    @validator('base_url')
    def base_url_len(cls, v: str):
        if len(v) < 2:
            raise ValueError(f'base url must have len >= {len(v)}')
        
        if 'https://discord' not in v or 'api' not in v:
            raise ValueError(f'base url must have right url {v}')
        
        return v
    

class Channel(BaseModel):
    id: int
    last_message_id: int|None
    type: int
    name: str
    position: int
    flags: int
    parent_id: int
    topic: int|None
    guild_id: int
    permission_overwrites: list|None
    rate_limit_per_user: int|None
    nsfw: bool

    async def send_message(self, content: str, embeds = []) -> None:
        from src.api.api import interface, API
        
        api: API = interface['api']
        api.create_message(self.id, content, embeds)