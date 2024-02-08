import os
from dataclasses import dataclass

from dotenv import load_dotenv


BotToken = str


@dataclass
class BotConfig:
    token: BotToken


class DotenvLoadException(Exception): ...


def get_bot_config_from_dotenv(path: str = ".env") -> BotConfig:
    is_load_success = load_dotenv(path)

    if not is_load_success:
        raise DotenvLoadException("Could not load dontenv file")

    token = os.getenv("BOT_TOKEN")

    if not token:
        raise DotenvLoadException("BOT_TOKEN should be specified")

    return BotConfig(token=token)
