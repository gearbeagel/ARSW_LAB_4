from abc import ABC
from typing import List


class Dish:
    def __init__(self, dish_name: str, dish_price: float):
        self.dish_name = dish_name
        self.dish_price = dish_price

    def __eq__(self, other):
        if isinstance(other, Dish):
            return self.dish_name == other.dish_name and self.dish_price == other.dish_price
        return False


class Menu:
    def __init__(self, dishes: List[Dish]):
        self.dishes = dishes

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def assure_dish(self, dish: Dish):
        return dish in self.dishes


class Client:
    def __init__(self, name: str):
        self.name = name


class Order(ABC):
    def __init__(self, orderer: Client, dishes: List[Dish]):
        self.orderer = orderer
        self.dishes = dishes

    def get_total_price(self):
        return sum([dish.dish_price for dish in self.dishes])


class SimpleOrder(Order):
    def __init__(self, orderer: Client, dishes: List[Dish]):
        super().__init__(orderer, dishes)


class BulkOrder(Order):
    def __init__(self, orderer: Client, dishes: List[Dish]):
        super().__init__(orderer, dishes)


