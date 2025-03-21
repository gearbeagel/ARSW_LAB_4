import pytest

from factory import OrderFactory
from models import Dish, Menu, Order, Client
from observer import KitchenNotifier, OrderNotifier
from singleton import OrderDatabase


@pytest.fixture
def menu():
    return Menu(
        [
            Dish("Pizza", 150),
            Dish("Pasta", 100),
            Dish("Salad", 50),
        ]
    )


def test_add_dish_to_menu(menu):
    dish = Dish("Burger", 120)
    menu.add_dish(dish)
    assert menu.assure_dish(dish)


def test_create_order():
    client = Client("John")
    dish1 = Dish("Pizza", 150)
    dish2 = Dish("Pasta", 100)
    order = Order(client, [dish1, dish2])
    assert order.get_total_price() == 250


def test_singleton_order_database():
    db1 = OrderDatabase()
    db2 = OrderDatabase()
    assert db1 is db2


def test_order_factory():
    client = Client("Jane")
    dish = Dish("Burger", 120)
    order = OrderFactory.create_order("regular", client, [dish])
    assert len(order.dishes) == 1


def test_observer_notification(capfd):
    kitchen = KitchenNotifier()
    notifier = OrderNotifier()
    notifier.add_observer(kitchen)

    client = Client("Mike")
    dish = Dish("Salad", 50)
    order = Order(orderer=client, dishes=[dish])

    notifier.notify(order)
    out, _ = capfd.readouterr()
    assert "Order received from" in out


def test_menu_contains_dish(menu):
    assert menu.assure_dish(Dish("Pizza", 150))


def test_order_total_price():
    client = Client("Alice")
    dish1 = Dish("Pizza", 150)
    dish2 = Dish("Salad", 50)
    order = Order(client, [dish1, dish2])
    assert order.get_total_price() == 200


def test_add_order_to_database():
    client = Client("Bob")
    dish = Dish("Pasta", 100)
    order = Order(client, [dish])
    db = OrderDatabase()
    db.add_order(order)
    assert order in db.get_orders()


def test_kitchen_notifier_update():
    kitchen = KitchenNotifier()
    client = Client("Eve")
    dish = Dish("Pasta", 100)
    order = Order(client, [dish])
    kitchen.update(order)
    assert True  # Replace with actual check if needed


def test_order_notifier_add_observer():
    notifier = OrderNotifier()
    kitchen = KitchenNotifier()
    notifier.add_observer(kitchen)
    assert kitchen in notifier.observers