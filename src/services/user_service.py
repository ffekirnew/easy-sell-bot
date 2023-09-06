from typing import List

from bson import ObjectId

from handlers.contracts.user_service_interface import UserServiceInterface
from models.user_model import User


class UserService(UserServiceInterface):
    def __init__(self):
        self.users = []

    def get_all_users(self) -> List[User]:
        return self.users

    def get_user(self, user_telegram_id: int):
        return User(
            _id=ObjectId(), telegram_id="123", telegram_username="123", phone="1234"
        )

    def user_exists(self, telegram_user_id: int):
        return True

    def get_user_by_telegram_id(self, telegram_id: str) -> User:
        for user in self.users:
            if user.telegramId == telegram_id:
                return user
        return None

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def update_user(self, telegram_id: str, updated_user: User) -> None:
        for i, user in enumerate(self.users):
            if user.telegramId == telegram_id:
                self.users[i] = updated_user
                return
