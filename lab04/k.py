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

    def buy(self, product, amount) -> bool:
        if amount >= 0:
            if amount <= product.amount_of_product:
                # print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona sukcesem.")
                product.amount_of_product -= amount
                self.amount += amount
                if product.name in self.product_dict:
                    self.product_dict[product.name] += amount
                else:
                    self.product_dict[product.name] = amount
                return True
            else:
                # print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona niepowodzeniem.")
                print(
                    f"Liczba dostępnych sztuk w magazynie to {product.amount_of_product}"
                )
                return False
        else:
            # print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona niepowodzeniem.")
            print(f"Nie można kupić ujemnej liczby produktu - {product.name}")
            return False

    def calculate_total_value(self, products):
        total_value = sum(
            self.product_dict.get(product.name, 0) * product.price for product in products
        )
        return total_value

    def __str__(self):
        return f"""
Klient {self.name} {self.surname} (ID: {self.client_id})
Ilość zakupionych produktów: {self.amount}
Wartość zakupów: {self.calculate_total_value(Store.products)} zł\n"""

    def __repr__(self):
        return f"{self.client_id}: {self.name} {self.surname}"


class Transaction:
    def __init__(self, client, product, date):
        self.client: Client = client
        self.product: Product = product
        self.date: datetime.date = date.today()

    def __str__(self):
        return f"""Data: {self.date}
Klient: {self.client}"""
# Produkt: {self.product}


class Store:
    products: list[Product] = [
        Product("Komputer", 7, 2000),
        Product("Laptop", 15, 5000),
        Product("Smartfon", 20, 1500),
        Product("Tablet", 10, 800),
    ]
    
    def __init__(self):
        self.transactions: list[Transaction] = []

    def sell_to_client(self, client_id, product_id, amount):
        client = next((transaction.client for transaction in self.transactions if transaction.client.client_id == client_id), None)
        try:
            product = self.products[product_id]
        except IndexError:
            print("Niepoprawny numer produktu!")
            return

        if client is None:
            client_name = input("Podanego klienta nie ma, podaj jego nazwę: ")
            # client_name = "Jan K"
            client = Client(client_name)
            
            purchased_products = client.buy(product, amount)
            if purchased_products:
                self.transactions.append(Transaction(client, product, date.today()))
                print("Transakacja się powiodła.")
            else:
                print("Transakacja się nie powiodła.")
        else:
            if client_id not in self.transactions:
                # client.buy(product, amount)
                purchased_products = client.buy(product, amount)
                if purchased_products:
                    self.transactions.append(Transaction(client, product, date.today()))
                    print("Transakacja się powiodła.")
                else:
                    print("Transakacja się nie powiodła.")
            else:
                self.transactions.pop()
                purchased_products = client.buy(product, amount)
                if purchased_products:
                    self.transactions.append(Transaction(client, product, date.today()))
                    print("Transakacja się powiodła.")
                else:
                    print("Transakacja się nie powiodła.")
        # for transaction in self.transactions:
        #     print("HEHE\n", transaction, "HEHE\n")


store = Store()
store.sell_to_client(0, 1, 2)
print(store.transactions[0])
store.sell_to_client(0, 1, 2)
print(store.transactions[0])
store.sell_to_client(1, 1, 2)
print(store.transactions[1])
print(store.transactions)
