from pydantic import BaseModel, validator


class Product(BaseModel):
    name: str = ""
    description: str = ""
    price: int = 0

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return self.dict()

    @validator("name")
    def validate_name(cls, value):
        if not value:
            raise ValueError("Product name cannot be empty")
        return value

    @validator("description")
    def validate_description(cls, value):
        if not value:
            raise ValueError("Product description cannot be empty")
        return value

    @validator("price")
    def validate_price(cls, value):
        if value < 0:
            raise ValueError("Product price cannot be negative")
        return value

    def add_name(self, name: str) -> "Product":
        self.name = self.validate_name(name)
        return self

    def add_description(self, description: str) -> "Product":
        self.description = self.validate_description(description)
        return self

    def add_price(self, price: int) -> "Product":
        self.price = self.validate_price(price)
        return self
