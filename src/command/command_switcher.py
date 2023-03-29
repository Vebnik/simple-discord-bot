from src.gateway.models.message_models import MessageEvent

from src.command.ping import Ping
from src.command.play import Play


class Switcher:

    @staticmethod
    async def commands(cmd: str, msg: MessageEvent) -> None:
        match cmd:
            case 'ping': Ping.init(msg)
            case 'play': await Play.init(msg)