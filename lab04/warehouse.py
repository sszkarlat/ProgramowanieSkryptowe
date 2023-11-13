from datetime import date
import json

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
    next_id = 0

    def __init__(self, name):
        self.id = Client.next_id
        self.name = name.split(" ")[0]
        self.surname = name.split(" ")[1]
        self.amount = 0
        self.products_value = 0
        self.product_dict = {}

        Client.next_id += 1

    def buy(self, product, amount) -> bool:
        if amount >= 0:
            if amount <= product.amount_of_product:
                product.amount_of_product -= amount
                self.amount += amount
                if product.name in self.product_dict:
                    self.product_dict[product.name] += amount
                    self.products_value = self.products_value + (product.price*amount)
                else:
                    self.product_dict[product.name] = amount
                    self.products_value = self.products_value + (product.price*amount)
                return True
            else:
                print(f"Liczba dostępnych sztuk w magazynie to {product.amount_of_product}")
                return False
        else:
            print(f"Nie można kupić ujemnej liczby produktu - {product.name}")
            return False

    def __str__(self):
        product_info = "\n".join(
            [
                f"Produkt: {name}, Ilość: {amount}"
                for name, amount in self.product_dict.items()
            ]
        )
        return f"""
Klient: {self.name} {self.surname} (ID: {self.id})
{product_info}
Wartość zakupów: {self.products_value} zł\n"""

    def __repr__(self):
        return f"{self.id}: {self.name} {self.surname}"


class Transaction:
    def __init__(self, client, product, date):
        self.client: Client = client
        self.product: Product = product
        self.date: datetime.date = date.today()

    def __str__(self):
        return f"Data: {self.date} {self.client}"


class Store:
    def __init__(self, json_file):
        self.products = self.load_products_from_json(json_file)
        self.transactions = []

    def load_products_from_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)

        products = []
        for product_data in data:
            product = Product(product_data['name'], product_data['amount_of_product'], product_data['price'])
            products.append(product)

        return products

    def sell_to_client(self, client_id, product_id, amount):
        client = next((transaction.client for transaction in self.transactions if transaction.client.id == client_id), None)
        try:
            product = self.products[product_id]
        except IndexError:
            print("Niepoprawny numer produktu!")
            return

        if client is None:
            client_name = input("Podanego klienta nie ma, podaj jego nazwę: ")
            try:
                int(client_name)
                print("Nazwa klienta powinna być napisem.")
                return
            except:
                client = Client(client_name)
            
            purchased_products = client.buy(product, amount)
            if purchased_products:
                self.transactions.append(Transaction(client, product, date.today()))
                print("Transakacja się powiodła.")
                list_of_clients.append(client)
            else:
                print("Transakacja się nie powiodła.")
        else:
                purchased_products = client.buy(product, amount)
                if purchased_products:
                    self.transactions[client_id - first_number_id] = Transaction(client, product, date.today())
                    print("Transakacja się powiodła.")
                else:
                    print("Transakacja się nie powiodła.")

    def add_product(self, name: str, amount: int, price: int):
        try:
            int(name)
            print("Nazwa produktu musi być napisem.")
        except:
            if amount > 0 and price > 0:
                new_product = Product(name, amount, price)
                self.products.append(new_product)
                self.save_to_json(json_file_path)
                print(f"Dodano nowy produkt: {new_product}")
            else:
                print("Nie dodano produktu, bo nie można dodać ujemnej liczby.")

    def save_to_json(self, json_file_path):
        data = [
            {
                "name": product.name,
                "amount_of_product": product.amount_of_product,
                "price": product.price
            }
            for product in self.products
        ]
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=2)

if __name__ == "__main__":
    list_of_clients = []
    json_file_path = "magazyn.json"  # Ścieżka do pliku JSON
    store = Store(json_file_path)

    try:
        while True:
            inputDataList = input("> ").split(" ")

            if inputDataList[0] == "warehouse":
                try:
                    print(store.products[int(inputDataList[1])])
                except IndexError:
                    print("WSZYSTKIE PRODUKTY!!!")
                    print("---------------------")
                    for product in store.products:
                        print(product)
            elif inputDataList[0] == "clients":
                print(list_of_clients)
            elif inputDataList[0] == "show":
                try:
                    difference = int(inputDataList[1]) - first_number_id
                    print(store.transactions[difference]) if 0 <= difference < len(list_of_clients)  else print("Niepoprawna komenda!")
                except:
                    print("WSZYSTKIE TRANSAKCJE!!!")
                    print("-----------------------")
                    for transaction in store.transactions:
                        print(transaction) 
                    
            elif inputDataList[0] == "sell":
                try:
                    if not list_of_clients:
                        if int(inputDataList[1]) < 0:
                            print("Id musi iść być liczba naturalną")
                        else:
                            first_number_id = int(inputDataList[1])
                            Client.next_id = first_number_id
                            store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                    else:
                        if int(inputDataList[1]) - Client.next_id == 0:
                            store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                        elif first_number_id <= int(inputDataList[1]) <= Client.next_id - 1:
                            store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                        else:
                            print("Id musi iść po kolei.")
                            print("Kolejne id: ", Client.next_id)
                       
                except (IndexError, ValueError):
                    print("Niepoprawna komenda!")

            elif inputDataList[0] == "add":
                try:
                    name = str(inputDataList[1])
                    amount = int(inputDataList[2])
                    price = int(inputDataList[3])
                    store.add_product(name, amount, price)
                except IndexError:
                    print("Niepoprawna komenda!")
                
            else:
                print("Nieznana komenda!")
    except EOFError:
        exit()