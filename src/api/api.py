import logging, pprint as pp

from src.api.request import Request
from src.api.api_collection import ChannelEnpoint, MessageEnpoint
from src.api.models.models import (
    ApiConfig, Channel
)
interface = { }


class API:
    api_version: str
    base_url: str
    token: str
    user_agent: str
    compare_url: str
    request: Request

    def __init__(self, config: ApiConfig) -> None:
        if not isinstance(config, ApiConfig):
            raise Exception('config must be instance at Config')
        
        self.api_version = config.api_version
        self.base_url = config.base_url
        self.token = config.token
        self.user_agent = f'DiscordBot ({config.base_url}, 1)'
        self.compare_url = f'{config.base_url}/{config.api_version}'
        self.request = Request(self.user_agent, self.token)

    def get_channel(self, channel_id: int) -> Channel:
        url = ChannelEnpoint.crud_channel(self.compare_url, channel_id)

        response = self.request.get(url=url)
        channel = Channel.parse_obj(response)

        return channel
    
    def create_ref_message(self, channel_id: int, ref_message_id: int, guild_id: int, content: str, embeds = []) -> None:
        url = MessageEnpoint.create(self.compare_url, channel_id)

        body = {
            "content": content,
            "tts": False,
            "embeds": embeds,
            "message_reference": {
                "message_id": ref_message_id,
                "guild_id": guild_id,
                "fail_if_not_exists": True,
            }
        }

        self.request.post(url, body=body)

    def create_message(self, channel_id: int, content: str, embeds = []) -> None:
        url = MessageEnpoint.create(self.compare_url, channel_id)

        body = {
            "content": content,
            "tts": False,
            "embeds": embeds,
        }

        self.request.post(url, body=body)


def initApi(config: ApiConfig) -> API:
    interface['api'] = API(config)
    return interface['api']