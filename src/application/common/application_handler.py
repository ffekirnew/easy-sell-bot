from abc import abstractmethod

import telebot
import telebot.types as types

from ui.create_buttons import create_buttons
from utils.next_step import next_step


class ApplicationHandler:
    def __init__(self, bot: telebot.TeleBot):
        self.bot = bot

    @abstractmethod
    def start_application(self, message):
        pass

    @abstractmethod
    def finish_application(self, message):
        pass

    def send_markdown_message(
        self,
        chat_id: int,
        text: str,
        reply_markup: types.ReplyKeyboardRemove = types.ReplyKeyboardRemove(),
    ) -> telebot.types.Message:
        sent_message = self.bot.send_message(
            chat_id, text, parse_mode="Markdown", reply_markup=reply_markup
        )
        return sent_message

    def send_markdown_message_with_buttons(
        self, chat_id: int, text: str, buttons: list[str], width: int
    ) -> None:
        markup = create_buttons(buttons, width)
        sent_message = self.bot.send_message(chat_id, text, reply_markup=markup)
        return sent_message

    def handle_error(self, chat_id, error_text, next_step_function):
        sent_message = self.send_markdown_message(chat_id, error_text)
        next_step(self.bot, sent_message, next_step_function)

    def next_step(self, message: telebot.types.Message, handler: callable) -> None:
        self.bot.register_next_step_handler(message, handler)
