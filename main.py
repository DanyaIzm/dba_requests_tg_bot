from typing import List
from config import get_bot_config_from_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
import asyncio


async def start_polling(dispatcher: Dispatcher, bots: List[Bot], *args, **kwargs):
    return await dispatcher.start_polling(*bots, *args, **kwargs)


def main() -> None:
    bot_config = get_bot_config_from_dotenv()

    bot = Bot(bot_config.token, parse_mode=ParseMode.HTML)

    dispatcher = Dispatcher()

    asyncio.run(start_polling(dispatcher, bots=[bot]))


if __name__ == "__main__":
    main()
