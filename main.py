from dotenv import load_dotenv; load_dotenv()
from os import getenv
import asyncio, logging, datetime as dt

from src.gateway.models.message_models import MessageEvent
from src.gateway.models.service_models import ReadyEvent

from src.gateway.config import Intents, Event
from src.discord.app import App



async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    app = App(
        token=getenv('BOT_TOKEN') or '',
        intents=[Intents.GUILD_MEMBERS, Intents.MESSAGE_CONTENT, Intents.GUILD_MESSAGES]
    )

    @app.event(Event.MESSAGE_CREATE)
    async def on_message(msg: MessageEvent) -> None:
        if msg.author.username == 'GitHub': return
        await msg.reply('Ping')

    @app.event(Event.READY)
    async def on_ready(msg: ReadyEvent) -> None:
        print(f'Bot {msg.user.username} started at {dt.datetime.now().isoformat(timespec="seconds")}')

    await app.run()

if __name__ == '__main__':
    asyncio.run(main())

