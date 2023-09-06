from telebot.custom_filters import SimpleCustomFilter
from tgbot.models.users_model import Admin


class AdminFilter(SimpleCustomFilter):
    key = "admin"

    def check(self, message):
        return int(message.chat.id) == int(Admin.ADMIN.value)
