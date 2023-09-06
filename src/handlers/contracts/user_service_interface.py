from abc import ABCMeta, abstractmethod

from bson import ObjectId

from models.user_model import User


class UserServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def user_exists(self, telegram_user_id: int) -> bool:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def add_user(self, user: User) -> ObjectId:
        pass
