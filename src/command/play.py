from src.gateway.models.message_models import MessageEvent


class Play:

    @staticmethod
    def valid_url(url: str) -> bool:
        return 'https://youtu.be/' in url

    @staticmethod
    async def init(msg: MessageEvent) -> None:
        args = msg.content.replace('~', '').split(' ')
        url = args[1]

        assert Play.valid_url(args[1])

        config = { 'guild_id': msg.guild_id, 'channel_id': 993069983481475133 }
        await msg.app.init_voice(url, config)

