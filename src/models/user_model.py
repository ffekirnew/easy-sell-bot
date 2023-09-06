from bson import ObjectId
from pydantic import BaseModel


class User(BaseModel):
    _id: ObjectId
    telegram_id: str
    telegram_username: str
    phone_number: int

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return self.dict()
