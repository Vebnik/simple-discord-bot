from websockets.legacy import client
import asyncio, json, logging
from typing import Any

from src.gateway.models.models import Config, InitMessage, IdentifyMessage
from src.gateway.handlers import EventHandler


class Gateway:

    connection: client.WebSocketClientProtocol
    config: Config
    heartbeat_interval: int
    identify_data: IdentifyMessage
    handlers_pool: dict[str, Any]

    def __init__(self, config: Config, logging_level: int, handlers_pool: dict[str, Any], app) -> None:
        self.config = config
        self.handlers_pool = handlers_pool
        self.app = app
        logging.basicConfig(level=logging_level)

    async def run(self):
        await self._gateway_connect()
        await self._identify()
        await asyncio.gather(*[self._event(), self._heartbeat()])

    async def _gateway_connect(self) -> None:
        try:
            logging.info('_gateway_connect')
            self.connection = await client.connect(self.config.wss_url)
            msg = InitMessage.parse_raw(await self.connection.recv())
            self.heartbeat_interval = msg.d.heartbeat_interval
        except Exception as ex:
             logging.critical(ex); exit()

    async def _heartbeat(self) -> None:
        while True:
            await asyncio.sleep(self.heartbeat_interval/1000)
            await self.connection.send(json.dumps({ "op": 1, "d": None }))
            logging.info('_heartbeat')
    
    async def _identify(self) -> None:
        logging.info('_identify')
        await self.connection.send(json.dumps(self.config.identify_data.dict()))

    async def _event(self) -> None:
        while True:
            try:
                msg: dict = json.loads(await self.connection.recv())

                if msg.get('t'):
                    asyncio.ensure_future(EventHandler.switcher(self.handlers_pool, msg, self.app)) # app instance App

                logging.info('_event')
            except Exception as ex:
                logging.critical(ex)
                continue

    async def _resume(self) -> None:
        logging.info('_resume')

    async def voice_state_update(self, config) -> None:
        logging.info('_voice_state_update')
        
        voice_payload = {
            "op": 4,
            "d": {
                "guild_id": config.get('guild_id'),
                "channel_id": "993069983481475133",
                "self_mute": False,
                "self_deaf": True
            }
        }

        await self.connection.send(json.dumps(voice_payload))