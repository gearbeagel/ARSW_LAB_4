from models import Dish, Menu, Client, SimpleOrder, BulkOrder
from singleton import OrderDatabase
from observer import KitchenNotifier, OrderNotifier


def main():
    pizza = Dish("Pizza", 150)
    pasta = Dish("Pasta", 100)
    salad = Dish("Salad", 50)

    menu = Menu([pizza, pasta, salad])
    print("Menu created with dishes:", [dish.dish_name for dish in menu.dishes])

    client = Client("John")

    order = SimpleOrder(client, [pizza, pasta])
    print(f"Order created for {client.name} with total price: {order.get_total_price()}")

    order_db = OrderDatabase()
    order_db.add_order(order)
    print("Order added to the database")

    kitchen_notifier = KitchenNotifier()
    order_notifier = OrderNotifier()
    order_notifier.add_observer(kitchen_notifier)
    order_notifier.notify(order)


if __name__ == "__main__":
    main()
