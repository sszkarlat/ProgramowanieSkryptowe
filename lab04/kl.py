from datetime import date

class Product:
    def __init__(self, name, amount_of_product, price):
        self.name = name
        self.amount_of_product = amount_of_product
        self.price = price

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"""
Produkt: {self.name}
Ilość: {self.amount_of_product}
Cena: {self.price} zł\n"""


class Client:
    nextClient_id = 0

    def __init__(self, name):
        self.client_id = Client.nextClient_id
        Client.nextClient_id += 1
        self.name = name.split(" ")[0]
        self.surname = name.split(" ")[1]
        self.amount = 0
        self.product_dict = {}

    def buy(self, product, amount):
        if amount >= 0:
            if amount <= product.amount_of_product:
                print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona sukcesem.")
                product.amount_of_product -= amount
                self.amount += amount
                if product.name in self.product_dict:
                    self.product_dict[product.name] += amount
                else:
                    self.product_dict[product.name] = amount
            else:
                print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona niepowodzeniem.")
                print(
                    f"Liczba dostępnych sztuk w magazynie to {product.amount_of_product}"
                )
        else:
            print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona niepowodzeniem.")
            print(f"Nie można kupić ujemnej liczby produktu - {product.name}")

    def calculate_total_value(self, products):
        total_value = sum(
            self.product_dict.get(product.name, 0) * product.price for product in products
        )
        return total_value

    def __repr__(self):
        return f"{self.client_id}: {self.name} {self.surname}"

    def __str__(self):
        product_info = "\n".join(
            [f"Produkt: {name}, Ilość: {amount}" for name, amount in self.product_dict.items()]
        )
        return f"{self.name} {self.surname}\n{product_info}\nWartość kupionych towarów wynosi {self.calculate_total_value(Store.products)} zł"


class Transaction:
    def __init__(self, client, product, date):
        self.client: Client = client
        self.product: Product = product
        self.date: datetime.date = date.today()

    def __str__(self):
        return f"{self.date}\nId: {self.client.client_id} {self.client}\n"


class Store:
    products: list[Product] = [
        Product("Komputer", 7, 2000),
        Product("Laptop", 15, 5000),
        Product("Smartfon", 20, 1500),
        Product("Tablet", 10, 800),
    ]
    transactions: list[Transaction] = []

    @classmethod
    def sell_to_client(cls, client_id, product_id, amount):
        client = next((transaction.client for transaction in cls.transactions if transaction.client.client_id == client_id), None)
        if client is None:
            client_name = input("Podanego klienta nie ma, podaj jego nazwę: ")
            client = Client(client_name)
            list_of_clients.append(client)

        try:
            product = cls.products[product_id]
        except IndexError:
            print("Niepoprawny numer produktu!")
            return

        client.buy(product, amount)
        transaction = Transaction(client, product, date.today())
        if cls.transactions == [] or transaction.date in cls.transactions:
            cls.transactions.append(transaction)
        else:
            cls.transactions.append(transaction)

if __name__ == "__main__":
    list_of_clients = []

    try:
        while True:
            inputDataList = input("> ").split(" ")

            if inputDataList[0] == "warehouse":
                try:
                    print(Store.products[int(inputDataList[1])])
                except IndexError:
                    for product in Store.products:
                        print(product)
            elif inputDataList[0] == "clients":
                print(list_of_clients)
            elif inputDataList[0] == "show":
                try:
                    for transaction in Store.transactions:
                        print(transaction)
                except IndexError:
                    print("Niepoprawna komenda!")
            elif inputDataList[0] == "sell":
                try:
                    Store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                except (IndexError, ValueError):
                    print("Niepoprawna komenda!")
            else:
                print("Nieznana komenda!")
    except EOFError:
        exit()