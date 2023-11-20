from datetime import date
import json



class Base:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price
    
    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"Cena: {self.price} zł"



# Klasa Service dziedziczy z klasy bazowej Base
class Service(Base):
    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)

    def __str__(self) -> str:
        return f"""
Usługa: {self.name}
""" + super().__str__()



# KLasa Product dziedziczy z klasy bazowej Base
class Product(Base):
    def __init__(self, name, amount_of_product, price):
        self.amount_of_product = amount_of_product
        super().__init__(name, price)

    def __str__(self) -> str:
        return f"""
Produkt: {self.name}
Ilość: {self.amount_of_product}
""" + super().__str__()



class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.amount = 0
        self.products_value = 0
        self.product_dict = {}


    def buy_product(self, product, amount) -> bool:
        if amount > 0:
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
        elif amount == 0:
            print(f"Nie można kupić zerowej liczby produktu - {product.name}")
            return False
        else:
            print(f"Nie można kupić ujemnej liczby produktu - {product.name}")
            return False


    def buy_service(self, product) -> bool:
        amount = 1
        if product.name in self.product_dict:
            self.product_dict[product.name] += amount
            self.products_value = self.products_value + (product.price*amount)
        else:
            self.product_dict[product.name] = amount
            self.products_value = self.products_value + (product.price*amount)
        return True


    def __eq__(self, other_client):
        if isinstance(other_client, Client):
            return self.name == other_client.name and self.surname == other_client.surname
        return False


    def __hash__(self):
        return hash((self.name, self.surname))


    def __str__(self):
        product_info = "\n".join(
            [
                f"Produkt albo usługa: {name}, Ilość: {amount}"
                for name, amount in self.product_dict.items()
            ]
        )
        return f"""
Klient: {self.name} {self.surname}
{product_info}
Wartość zakupów: {self.products_value} zł\n"""


    def __repr__(self):
        return f"{self.name} {self.surname}"



class Transaction:
    def __init__(self, product, date):
        self.product = product
        self.date: datetime.date = date.today()

    def __str__(self):
        return f"Data: {self.date} | Produkt/Usługa: {self.product.name}"



class Store:
    def __init__(self, clients: dict[Client, list[Transaction]], product_json, service_json):
        self.list_of_products, self.list_of_services = self.load_data_from_json(product_json, service_json)
        self.clients = clients
        self.transactions = []


    def load_data_from_json(self, product_json, service_json):
        with open(product_json, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        list_of_products = []
        for product_data in data:
            product = Product(product_data['name'], product_data['amount_of_product'], product_data['price'])
            list_of_products.append(product)

        with open(service_json, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        list_of_services = []
        for service_data in data:
            service = Service(service_data['name'], service_data['price'])
            list_of_services.append(service)

        return list_of_products, list_of_services


    def sell_product_to_client(self, client_name, client_surname, product_id, amount):
        found_client = None
        try:
            product = self.list_of_products[product_id]
        except IndexError:
            print("Niepoprawny numer produktu!")
            return
            
        for existing_client in self.clients:
            newClient = Client(client_name, client_surname)
            if existing_client.__eq__(newClient):
                found_client = existing_client
                break

        if found_client is None:
            newClient = Client(client_name, client_surname)
            self.clients[newClient] = []

            purchased_products = newClient.buy_product(product, amount)
            if purchased_products:
                self.transactions.append((str(Transaction(product, date.today())) + " | Ilość: " + str(amount)))
                self.clients[newClient].append((str(Transaction(product, date.today())) + " | Ilość: " + str(amount)))
                list_of_clients.append(newClient)
                print("Transakacja się powiodła.")
            else:
                print("Transakcja się nie powiodła.")
        else:
            purchased_products = found_client.buy_product(product, amount)
            if purchased_products:
                self.transactions.append((str(Transaction(product, date.today())) + " | Ilość: " + str(amount)))
                self.clients[newClient].append((str(Transaction(product, date.today())) + " | Ilość: " + str(amount)))
                print("Transakcja się powiodła.")
            else:
                print("Transakcja się nie powiodła.")


    def sell_service_to_client(self, client_name, client_surname, service_id):
        found_client = None
        try:
            service = self.list_of_services[service_id]
        except IndexError:
            print("Niepoprawny numer usługi!")
            return
            
        for existing_client in self.clients:
            newClient = Client(client_name, client_surname)
            if existing_client.__eq__(newClient):
                found_client = existing_client
                break

        if found_client is None:
            newClient = Client(client_name, client_surname)
            self.clients[newClient] = []

            purchased_services = newClient.buy_service(service)
            if purchased_services:
                self.transactions.append(Transaction(service, date.today()))
                self.clients[newClient].append(Transaction(service, date.today()))
                list_of_clients.append(newClient)
                print("Transakacja się powiodła.")
            else:
                print("Transakcja się nie powiodła.")
        else:
            purchased_services = found_client.buy_service(service)
            if purchased_services:
                self.transactions.append(Transaction(service, date.today()))
                self.clients[found_client].append(Transaction(service, date.today()))
                print("Transakcja się powiodła.")
            else:
                print("Transakcja się nie powiodła.")


if __name__ == "__main__":
    product_json = "products.json"  # Ścieżka do pliku JSON (produkty)
    service_json = "services.json"  # Ścieżka do pliku JSON (uslugi)
    client = Client("Szymon", "Szkarłat")
    clients = {client: []}
    list_of_clients = [client for client in clients]
    store = Store(clients, product_json, service_json)

    try:
        while True:
            inputDataList = input("> ").split(" ")

            if inputDataList[0] == "warehouse":
                try:
                    if inputDataList[1] == "product":
                        print(store.list_of_products[int(inputDataList[2])])
                    elif inputDataList[1] == "service":
                        print(store.list_of_services[int(inputDataList[2])])
                except IndexError:
                    print("WSZYSTKIE PRODUKTY!!!")
                    print("---------------------")
                    print(store.list_of_products)
                    for product in store.list_of_products:
                        print(product)
                    print("\n\nWSZYSTKIE USŁUGI!!!")
                    print("---------------------")
                    print(store.list_of_services)
                    for service in store.list_of_services:
                        print(service)
                        
            elif inputDataList[0] == "clients":
                print("Brak klientów") if not list_of_clients else print(list_of_clients)

            elif inputDataList[0] == "show":
                try:
                    for client in store.clients.keys():
                        if client.__eq__(Client(inputDataList[1], inputDataList[2])):
                            if store.clients[client]:
                                for transaction in store.clients[client]:
                                    print(transaction)
                            else:
                                print("Brak transakcji")
                except:
                    if store.transactions:
                        for transaction in store.transactions:
                            print(transaction)
                    else:
                        print("Brak transakcji")

            elif inputDataList[0] == "show_details":
                try:
                    for client in store.clients:
                        if client.__eq__(Client(inputDataList[1], inputDataList[2])):
                            print(client)
                except:
                    for clientTransactions in store.clients:
                        print(clientTransactions)
                    
            elif inputDataList[0] == "sell":
                # print(inputDataList)
                try:
                    if inputDataList[1] == "product":
                        store.sell_product_to_client(inputDataList[2], inputDataList[3], int(inputDataList[4]), int(inputDataList[5]))
                    elif inputDataList[1] == "service":
                        store.sell_service_to_client(inputDataList[2], inputDataList[3], int(inputDataList[4]))
                except (IndexError, ValueError):
                    print("Niepoprawna komenda!")             
            else:
                print("Nieznana komenda!")
    except EOFError:
        exit()
