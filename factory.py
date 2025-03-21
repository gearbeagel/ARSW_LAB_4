from typing import List

from models import Order, Client, Dish


class OrderFactory:
    @staticmethod
    def create_order(order_type: str, client: Client, dishes: List[Dish]) -> Order:
        if order_type == "regular":
            return Order(client, dishes)
        elif order_type == "bulk":
            return Order(client, dishes * 2)
        else:
            raise ValueError("Unknown order type")