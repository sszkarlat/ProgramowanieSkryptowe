import datetime
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
    products: list[Product] = []

    def __init__(self):
        self.transactions: list[Transaction] = []

    def add_product(self, product):
        self.products.append(product)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def to_json(self):
        return json.dumps({
            'products': [product.to_json() for product in self.products],
            'transactions': [transaction.to_json() for transaction in self.transactions]
        })

    @classmethod
    def from_json(cls, file_path):
        with open(file_path) as file:
            data = json.load(file)

        transactions = [Transaction(**transaction_data) for transaction_data in data['transactions']]

        store_instance = cls()
        store_instance.products = products
        store_instance.transactions = transactions

        return store_instance

class Transaction:
    def __init__(self, client, product, date):
        self.client: Client = client
        self.product: Product = product
        self.date: datetime.date = date

    def to_json(self):
        return {
            'client': self.client.to_json(),
            'product': self.product.to_json(),
            'date': str(self.date)
        }

    @classmethod
    def from_json(cls, data):
        client = Client(**data['client'])
        product = Product(**data['product'])
        date = date.fromisoformat(data['date'])

        return cls(client=client, product=product, date=date)


class Client:
    nextId = 1 # Zmienna klasowa - przechowuje wartość id następnego klienta
    def __init__(self, name):
        self.id = Client.nextId # Zmienna instancyjna - przypisanie id do konkretnego klienta
        self.surname = name.split(" ")[1]
        self.name = name.split(" ")[0]
        self.amount = 0
        self.productDict = {}
        
        Client.nextId += 1 # Zwiększenie id (zmiennej klasowej dla kolejnego klienta)

    def buy(self, product, amount):
        if amount >= 0:
            if amount <= product.amountOfProduct:
                product.amountOfProduct -= amount
                self.amount += amount
                if product.name in self.productDict:
                    self.productDict[product.name] += amount
                else:
                    self.productDict[product.name] = amount
            else:
                print(
                    f"Liczba dostępnych sztuk w magazynie to {product.amountOfProduct}"
                )
        else:
            print(f"Nie można kupić ujemnej liczby produktu - {product.name}")

    def __repr__(self):
        return self.name + " " + self.surname + " " + str(self.id)

    def calculate_total_value(self, product):
        if product == "Komputer":
            return (
                self.productDict.get("Komputer", 0)
                * list_of_products_in_warehouse[0].price
            )
        elif product == "Laptop":
            return (
                self.productDict.get("Laptop", 0)
                * list_of_products_in_warehouse[1].price
            )
        return 0

    def __str__(self):
        total_value = sum(
            self.calculate_total_value(product) for product in ["Komputer", "Laptop"]
        )
        product_info = "\n".join(
            [
                f"Produkt:{name}, Ilość:{amount}"
                for name, amount in self.productDict.items()
            ]
        )

        return f"{self.name}\n{product_info}\nWartość kupionych towarów wynosi {total_value} zł"

list_of_clients = [Client("Jan Kowalski"), Client("Anna Nowak")]
store = Store.from_json('magazyn.json')

if __name__ == "__main__":
    try:
        while True:
            inputDataList = input("> ").split(" ")
            if inputDataList[0] == "warehouse":
                try:
                    if any(product.name == inputDataList[1] for product in store.products):
                    print(pr)
                except IndexError:
                    for product in store:
                        print(product)
            elif inputDataList[0] == "clients":
                print(list_of_clients)
            elif inputDataList[0] == "show":
                try:
                    print(list_of_clients[int(inputDataList[1])])
                except IndexError:
                    print(list_of_products_in_warehouse[0], list_of_products_in_warehouse[1])
            elif inputDataList[0] == "sell":
                try:
                    list_of_clients[int(inputDataList[1])].buy(
                        list_of_products_in_warehouse[int(inputDataList[2])],
                        int(inputDataList[3]),
                    )
                except IndexError:
                    print("Niepoprawna komenda!")
            elif inputDataList[0] == "add":
                try:
                    product = Product(inputDataList[1], inputDataList[2], inputDataList[3])
                    product.to_json()
                except IndexError:
                    print("Należy podać: nazwę produktu, liczba sztuk, cena za sztukę.")
            else:
                print("Nieznana komenda!")
    except EOFError:
        exit
