from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove

from handlers.common.base_handler import BaseHandler
from models.product_model import Product


class AddProduct(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)
        self.product = Product()
        self.remove_keyboard_markup = ReplyKeyboardRemove()

    def start(self, message: Message) -> None:
        text = (
            "Listing a product on our platform is easy."
            " Send the *name* of the product now."
        )
        sent_message = self.send_markdown_message(message.chat.id, text)
        self.pass_to_next_handler(sent_message, self.get_product_name)

    def get_product_name(self, message: Message) -> None:
        try:
            self.product.add_name(message.text)

            text = "Now send the *description* for your product."
            sent_message = self.send_markdown_message(message.chat.id, text)
            self.pass_to_next_handler(sent_message, self.get_product_description)
        except ValueError:
            error_message = "Name cannot be empty. Send the name of the product now."
            self.handle_error(message.chat.id, error_message, self.get_product_name)

    def get_product_description(self, message: Message) -> None:
        try:
            self.product.add_description(message.text)

            text = "Now send the price for your product."
            sent_message = self.send_markdown_message(message.chat.id, text)
            self.pass_to_next_handler(sent_message, self.get_product_price)
        except ValueError:
            error_message = (
                "Description cannot be empty. Send the description for your product."
            )
            self.handle_error(
                message.chat.id, error_message, self.get_product_description
            )

    def get_product_price(self, message: Message) -> None:
        try:
            self.product.add_price(int(message.text))

            text = (
                "You have added the following product:"
                f" \n {self.product}.\nConfirmed?"
            )
            sent_message = self.send_markdown_message_with_buttons(
                message.chat.id, text, ["Yes", "No"], 2
            )
            self.pass_to_next_handler(sent_message, self.finish)
        except ValueError:
            error_message = (
                "Price needs to be a number greater than *0*. "
                "Set the price for your product accordingly."
            )
            self.handle_error(message.chat.id, error_message, self.get_product_price)

    def finish(self, message: Message) -> None:
        if message.text == "Yes":
            text = "Your product has been added to our platform."
            self.bot.send_message(
                message.chat.id, text, reply_markup=self.remove_keyboard_markup
            )
        else:
            text = (
                "Your product has not been added to our platform."
                " You can start again by typing in /add_product."
            )
            self.send_message(
                message.chat.id, text, reply_markup=self.remove_keyboard_markup
            )
