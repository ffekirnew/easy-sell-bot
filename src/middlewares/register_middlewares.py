from telebot import TeleBot

from middlewares.antiflood.antiflood_middleware import antiflood_middleware


class RegisterMiddlewares:
    def __init__(self, bot: TeleBot):
        # Instantiate handlers
        self.bot = bot

    def register_middlewares(self) -> None:
        self.bot.register_middleware_handler(
            antiflood_middleware
        )
