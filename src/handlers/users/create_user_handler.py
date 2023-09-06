from telebot import TeleBot
from telebot.types import Message

from handlers.common.base_handler import BaseHandler
from handlers.contracts.user_service_interface import UserServiceInterface


class CreateUsersHandler(BaseHandler):
    def __init__(self, bot: TeleBot, userService: UserServiceInterface):
        super.__init__(bot)
        self._userService = userService

    def start(self, message: Message) -> None:
        pass

    def get_user_choice(self, message: Message) -> None:
        pass

    def finish(self, message: Message) -> None:
        pass
