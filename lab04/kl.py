# class Number:
#     nextId = 1
#     def __init__(self):
#         self.id = Number.nextId
#         Number.nextId += 1

#     def __str__(self):
#         return str(self.id)

# numberList = [Number() for _ in range(10)]
# for number in numberList:
#     print(number)

import json

class Product:
    def __init__(self, name, amountOfProduct, price):
        self.name = name
        self.amountOfProduct = amountOfProduct
        self.price = price

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"""
Produkt: {self.name}
Ilość: {self.amountOfProduct}
Cena: {self.price} zł\n"""

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)


class Store:
    def __init__(self, products=None):
        self.products = products or []

    def add_product(self, product):
        self.products.append(product)

    def to_json(self):
        return json.dumps([product.to_json() for product in self.products])

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        products = [Product(**product_data) for product_data in data['products']]
        return cls(products=products)

# Przykład użycia:

# Tworzenie nowego sklepu z danymi wczytanymi z pliku JSON
# Przykład użycia:

# Tworzenie nowego sklepu z danymi wczytanymi z pliku JSON
store = Store.from_json('magazyn.json')

# Sprawdzenie, czy produkt "Laptop" znajduje się w magazynie
product_name_to_find = "Laptop"
is_product_in_stock = any(product.name == product_name_to_find for product in store.products)

if is_product_in_stock:
    print(f"{product_name_to_find} jest dostępny w magazynie.")
else:
    print(f"{product_name_to_find} nie jest dostępny w magazynie.")

# Wyświetlanie produktów w sklepie
# for product in :
#     print(product.name)

    # def __init__(self, transactions: list[Transaction]):
    #     self.transactions = transactions

# class Transaction:
#     def __init__(self, client: Client, product: Product, date: datetime.date):
#         self.client = client
#         self.product = product
#         self.date = date


# list_of_products_in_warehouse = 
print()