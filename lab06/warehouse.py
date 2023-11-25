import argparse
import logging
import datetime
import json
from datetime import date


class AccessError(Exception):
    pass


def admin(func):
    def wrapper(*args, **kwargs):
        if isinstance(args[0], Client) and args[0].name.startswith("admin_"):
            return func(*args, **kwargs)
        else:
            raise AccessError("Access denied. Only admin users allowed.")
    return wrapper


def user(user):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logging.info(f"{datetime.datetime.now()}: User {user} called method {
                func.__name__} of class {args[0].__class__.__name__}")
            return result
        return wrapper
    return decorator


class Base:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"Cena: {self.price} zł"


# KLasa Product dziedziczy z klasy bazowej Base
class Product(Base):
    def __init__(self, name, amount_of_product, price):
        self.amount_of_product = amount_of_product
        super().__init__(name, price)

    @admin
    def __str__(self) -> str:
        return f"""
Produkt: {self.name}
Ilość: {self.amount_of_product}
""" + super().__str__()


class Transaction:
    def __init__(self, product, date):
        self.product = product
        self.date: datetime.date = date.today()

    @user("szymon12")
    def __str__(self):
        return f"Data: {self.date} | Produkt: {self.product.name}"


class Client:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    @user("szymon12")
    def buy_product(self, product, amount):
        return ((amount > 0 and ((amount <= product.amount_of_product and True) or (print(f"Liczba sztuk w magazynie: {product.amount_of_product}") and False))) or (amount == 0 and print(
            f"Nie można kupić zerowej liczby produktu - {product.name}") and False) or (amount < 0 and print(f"Nie można kupić ujemnej liczby produktu - {product.name}") and False))

    @user("szymon12")
    def __eq__(self, other_client):
        return (self.name == other_client.name and isinstance(other_client, Client))

    def __hash__(self):
        return hash(self.name)

    @admin
    def __str__(self):
        return f"Klient: {self.name}"

    def __repr__(self):
        return f"{self.name}"


class Store:
    def __init__(self, clients: dict[Client, list[Transaction]], product_json):
        self.list_of_products = self.load_data_from_json(product_json)
        self.clients = clients
        self.transactions = []

    def load_data_from_json(self, product_json):
        with open(product_json, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        return [Product(item['name'], item['amount_of_product'], item['price']) for item in data]

    def sell_product_to_client(self, client_name, product_id, amount):
        try:
            product = self.list_of_products[product_id]
        except IndexError:
            print("Niepoprawny numer produktu!")
            return

        new_client = Client(client_name)

        def purchase_and_update(transaction_list, client_list):
            transaction_list.append(
                (str(Transaction(product, date.today())) + " | Ilość: " + str(amount)))
            client_list.append(
                (str(Transaction(product, date.today())) + " | Ilość: " + str(amount)))
            print("Transakacja się powiodła!")

        (new_client not in self.clients and []) or (self.clients[new_client])
        (new_client.buy_product(product, amount) == True and purchase_and_update(
            self.transactions, self.clients[new_client]))


if __name__ == "__main__":
    logging.basicConfig(filename="warehouse_log.log", level=logging.INFO)

    # Argument parsing
    parser = argparse.ArgumentParser(description='Welcome to the warehouse!')
    parser.add_argument(
        '-f', '--file', help='Path to file.json', required=True)
    parser.add_argument('-c', '--client', help='client', required=True)
    parser.add_argument('-s', '--sell', help='Product that the customer bought',
                        nargs=2, action='extend', dest='product',  required=False)
    parser.add_argument('-sh', '--show', help='Show transactions by name',
                        action='store_true', required=False)
    parser.add_argument('-w', '--warehouse', help='Display warehouse status',
                        action='store_true', required=False)
    args = parser.parse_args()

    print(args)

    client = Client(args.client)
    clients = {client: []}
    list_of_clients = [client for client in clients]
    store = Store(clients, args.file)

    if "szymon12" != args.client:
        raise AccessError(f"Access denied. Only {
            "szymon12"} users allowed.")

    args.product and store.sell_product_to_client(
        args.client, int(args.product[0]), int(args.product[1]))
    args.show and print(store.clients.get(client))
    args.warehouse and print(store.list_of_products)

    # To może zrobić jedynie admin
    print(Product("Telewizor", 10, 2000))
