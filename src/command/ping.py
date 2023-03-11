from src.gateway.models.message_models import MessageEvent


class Ping:
    @staticmethod
    def init(msg: MessageEvent) -> None:
        msg.reply('Pong')