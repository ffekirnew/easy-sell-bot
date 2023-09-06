from telebot import TeleBot
from telebot.types import Message

from handlers.common.base_handler import BaseHandler
from handlers.contracts.user_service_interface import UserServiceInterface
from handlers.users.create_user_handler import CreateUsersHandler


class UsersHandler(BaseHandler):
    def __init__(self, bot: TeleBot, userService: UserServiceInterface):
        super.__init__(bot)
        self._userService = userService
        self.creat_user_handler = CreateUsersHandler(bot, userService)

    def start(self, message: Message) -> None:
        user_exists = self._userService.user_exists(message.chat.id)

        if user_exists:
            sent_message = self.send_markdown_message_with_buttons(
                message.chat.id,
                "Hello user, what do you want to do today?",
                ["See Products", "Sell a Product"],
                3,
            )
            self.pass_to_next_handler(sent_message, self.get_user_choice)
        else:
            self.creat_user_handler.start(message)

    def get_user_choice(self, message: Message) -> None:
        if message.text == "See Products":
            pass
        elif message.text == "Sell a Product":
            pass
        else:
            sent_message = self.send_markdown_message_with_buttons(
                message.chat.id,
                "We will try to add that choice, but we currently only have two choices.",
                ["See Products", "Sell a Product"],
            )
            self.pass_to_next_handler(sent_message, self.get_user_choice)

    def finish(self, message: Message) -> None:
        pass
