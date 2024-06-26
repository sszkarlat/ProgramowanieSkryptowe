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
    nextClient_id = 0

    def __init__(self, name):
        self.client_id = Client.nextClient_id
        Client.nextClient_id += 1
        self.name = name.split(" ")[0]
        self.surname = name.split(" ")[1]
        self.amount = 0
        self.products_value = 0
        self.product_dict = {}

    def buy(self, product, amount) -> bool:
        if amount >= 0:
            if amount <= product.amount_of_product:
                # print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona sukcesem.")
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
                # print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona niepowodzeniem.")
                print(
                    f"Liczba dostępnych sztuk w magazynie to {product.amount_of_product}"
                )
                return False
        else:
            # print(f"Transakcja dla {self.name} {self.surname} na produkt: {product.name} (w ilości: {amount}) zakończona niepowodzeniem.")
            print(f"Nie można kupić ujemnej liczby produktu - {product.name}")
            return False

    # def calculate_total_value(self, products):
    #     total_value = sum(
    #         self.product_dict.get(product.name, 0) * product.price for product in products
    #     )
    #     return total_value

    def __str__(self):
        product_info = "\n".join(
            [
                f"Produkt: {name}, Ilość: {amount}"
                for name, amount in self.product_dict.items()
            ]
        )
        return f"""
Klient: {self.name} {self.surname} (ID: {self.client_id})
{product_info}
Wartość zakupów: {self.products_value} zł\n"""

    def __repr__(self):
        return f"{self.client_id}: {self.name} {self.surname}"


class Transaction:
    def __init__(self, client, product, date):
        self.client: Client = client
        self.product: Product = product
        self.date: datetime.date = date.today()

    def __str__(self):
        return f"Data: {self.date} {self.client}"
# Produkt: {self.product}


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
                list_of_clients.append(client)
                # Client.nextClient_id += 1
            else:
                print("Transakacja się nie powiodła.")
                # Store.remove_last_client
                # Dodaj opcję usuwania ostatnio utworzonego obiektu klient
        else:
            # if client_id not in self.transactions:
                # client.buy(product, amount)
                purchased_products = client.buy(product, amount)
                if purchased_products:
                    self.transactions[client_id - first_number_id] = Transaction(client, product, date.today())
                    print("Transakacja się powiodła.")
                    # list_of_clients.append(client)
                    # Client.nextClient_id += 1
                else:
                    # Store.remove_last_client
                    print("Transakacja się nie powiodła.")
            # else:
            #     purchased_products = client.buy(product, amount)
            #     if purchased_products:
            #         self.transactions[client_id - first_number_id] = Transaction(client, product, date.today())
            #         print("Transakacja się powiodła.")
                    # list_of_clients.append(client)
                    # Client.nextClient_id += 1
                # else:
                #     # Store.remove_last_client
                #     print("Transakacja się nie powiodła.")

    # def remove_last_client(self):
    #     if self.transactions:
    #         removed_transaction = self.transactions.pop()
    #         last_client = removed_transaction.client
    #         list_of_clients.remove(last_client)
                
        # for transaction in self.transactions:
        #     print("HEHE\n", transaction, "HEHE\n")

    def add_product(self, name, amount, price):
        new_product = Product(name, amount, price)
        self.products.append(new_product)
        print(f"Dodano nowy produkt: {new_product}")

if __name__ == "__main__":
    list_of_clients = []
    json_file_path = 'magazyn.json'  # Zmień ścieżkę do pliku JSON na właściwą
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
                            Client.nextClient_id = first_number_id
                            store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                    else:
                        if int(inputDataList[1]) - Client.nextClient_id == 0:
                            store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                            # store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                        elif first_number_id <= int(inputDataList[1]) <= Client.nextClient_id - 1:
                            store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                        else:
                            print("Id musi iść po kolei.")
                            print("Kolejne id: ", Client.nextClient_id)
                        # elif int(inputDataList[1]) in list_of_clients:
                        #     store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                        # else:
                        #     print("Id musi iść po kolei")
                       
                except (IndexError, ValueError):
                    print("Niepoprawna komenda!")

            elif inputDataList[0] == "add":
                try:
                    name = inputDataList[1]
                    amount = int(inputDataList[2])
                    price = int(inputDataList[3])
                    store.add_product(name, amount, price)
                except (IndexError, ValueError):
                    print("Niepoprawna komenda!")            
                
            else:
                print("Nieznana komenda!")
    except EOFError:
        exit()