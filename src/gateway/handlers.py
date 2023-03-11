import logging
from typing import Any

from src.gateway.config import Event
from src.gateway.models.message_models import MessageEvent
from src.gateway.models.service_models import ReadyEvent

from src.voice_gateway.models import VoiceUpdateEvent


class EventHandler:

    @staticmethod
    async def switcher(handlers_pool: dict[str, Any], event, app) -> None:
        try:
            match event.get('t'):
                case Event.MESSAGE_CREATE:
                    msg = MessageEvent.parse_obj(event.get('d')); msg.app = app
                    await handlers_pool[event.get('t')](msg)
                case Event.READY:
                    await handlers_pool[event.get('t')](ReadyEvent.parse_obj(event.get('d')))
                case Event.VOICE_SERVER_UPDATE:
                    voice_config = VoiceUpdateEvent.parse_obj(event)
                    await app.init_voice_gateway(voice_config)
        except Exception as ex:
            logging.critical(ex)