from telebot import TeleBot

from handlers.products.add_product_handler import AddProduct
from handlers.users.user_handler import UsersHandler
from services.user_service import UserService


class RegisterHandlers:
    def __init__(self, bot: TeleBot):
        # Instantiate handlers
        self.bot = bot
        self._user_service = UserService()

    def register_handlers(self) -> None:
        self.bot.register_message_handler(
            AddProduct(self.bot).start, commands=["add_product"]
        )

        self.bot.register_message_handler(
            UsersHandler(self.bot, self._user_service).start, commands=["account"]
        )
