from abc import ABC, abstractmethod
from typing import List

from models import Order


class Observer(ABC):
    @abstractmethod
    def update(self, order: Order):
        pass


class KitchenNotifier(Observer):
    def update(self, order: Order):
        print(f"Order received from {order.orderer.name}: {[dish.dish_name for dish in order.dishes]}")


class OrderNotifier:
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, order: Order):
        for observer in self.observers:
            observer.update(order)
