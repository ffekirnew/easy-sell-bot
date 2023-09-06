from telebot import TeleBot

from handlers.product.add_product import AddProduct


class RegisterHandlers:
    def __init__(self, bot: TeleBot):
        # Instantiate handlers
        self.bot = bot
        self.add_product_handler = AddProduct(bot)

    def register_handlers(self) -> None:
        self.bot.register_message_handler(
            self.add_product_handler.start, commands=["add_product"]
        )
