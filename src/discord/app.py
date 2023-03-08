from typing import Any
import logging

from src.gateway.gateway import Gateway
from src.gateway.models.models import Config, IdentifyData, IdentifyDataToken

from src.api.api import initApi
from src.api.models.models import ApiConfig

class App:

    gateway: Gateway
    handlers_pool: dict[str, Any] = {}

    def __init__(self, token: str, intents: list[int]) -> None:
        try:
            self.identity_data = IdentifyData(
                d=IdentifyDataToken(
                    token=token, 
                    intents=sum(intents)
                )
            )

            self.config = Config( 
                wss_url='wss://gateway.discord.gg?v=10&encoding=json', 
                bot_token=token,
                identify_data=self.identity_data
            )

            self.api_config = ApiConfig(
                api_version='v10',
                base_url='https://discord.com/api',
                token=token
            )

        except Exception as ex:
            print(ex)

    async def run(self) -> None:
        self.api = initApi(self.api_config)
        self.gateway = Gateway(self.config, logging.INFO, self.handlers_pool)
        await self.gateway.run()
    
    def event(self, event: str) -> Any:
        def wrapper(func):
            logging.info(f'bind {event} at {func.__name__}')
            self.handlers_pool[event] = func
        return wrapper
    
    def get_handlers_pool(self) -> dict:
        return self.handlers_pool
    
        
