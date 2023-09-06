from abc import ABCMeta, abstractmethod

from telebot import TeleBot
from telebot.types import Message

from ui.create_buttons import create_buttons


class BaseHandler(metaclass=ABCMeta):
    def __init__(self, bot: TeleBot):
        self.bot = bot

    @abstractmethod
    def start(self, message: Message) -> None:
        pass

    @abstractmethod
    def finish(self, message: Message) -> None:
        pass

    def send_markdown_message(
        self,
        chat_id: int,
        text: str,
    ) -> Message:
        sent_message = self.bot.send_message(chat_id, text, parse_mode="Markdown")
        return sent_message

    def send_markdown_message_with_buttons(
        self,
        chat_id: int,
        text: str,
        buttons: list[str],
        width: int,
    ) -> Message:
        markup = create_buttons(buttons, width)
        sent_message = self.send_markdown_message(chat_id, text, markup)
        return sent_message

    def handle_error(
        self, chat_id: int, error_text: str, next_step_function: callable
    ) -> None:
        sent_message = self.send_markdown_message(chat_id, error_text)
        self.pass_to_next_handler(self.bot, sent_message, next_step_function)

    def pass_to_next_handler(self, message: Message, handler: callable) -> None:
        self.bot.register_next_step_handler(message, handler)
