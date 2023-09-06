from abc import ABCMeta, abstractmethod
from typing import List

from bson import ObjectId

from models.product_model import Product


class ProductServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def add_product(self, product: Product) -> ObjectId:
        pass

    @abstractmethod
    def update_product(self, product_id: ObjectId, updated_product: Product) -> None:
        pass
