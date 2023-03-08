import logging
from typing import Any

from src.gateway.config import Event
from src.gateway.models.message_models import MessageEvent


class EventHandler:

    @staticmethod
    async def switcher(handlers_pool: dict[str, Any], event) -> None:
        try:
            match event.get('t'):
                case Event.MESSAGE_CREATE:
                    await handlers_pool[event.get('t')](MessageEvent.parse_obj(event.get('d')))
                case Event.READY:
                    await handlers_pool[event.get('t')](event.get('d', {'message': False}))
        except Exception as ex:
            logging.critical(ex)