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
    # next_id = 0

    def __init__(self, name, surname):
        # self.id = Client.next_id
        self.name = name
        self.surname = surname
        self.amount = 0
        self.products_value = 0
        self.product_dict = {}

        # Client.next_id += 1

    def buy(self, product, amount) -> bool:
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
        self.product: Product = product
        self.date: datetime.date = date.today()

    def __str__(self):
        return f"Data: {self.date}"


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


    def sell_to_client(self, kind_of_product, client_name, client_surname, product_id, amount=0):
        found_client = None
        try:
            if kind_of_product == "product":
                product = self.list_of_products[product_id]
            elif kind_of_product == "service":
                product = self.list_of_services[product_id]
        except IndexError:
            print("Niepoprawny numer produktu!")
            return
            
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
    # next_id = 0

    def __init__(self, name, surname):
        # self.id = Client.next_id
        self.name = name
        self.surname = surname
        self.amount = 0
        self.products_value = 0
        self.product_dict = {}

        # Client.next_id += 1

    def buy(self, product, amount) -> bool:
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
                f"Produkt: {name}, Ilość: {amount}"
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
        return f"Data: {self.date}"


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
            if any(part.isdigit() for part in client_name.split(" ")):
                print("Nazwa klienta powinna być napisem.")
                return

            purchased_products = newClient.buy(product, amount)
            if purchased_products:
                self.transactions.append(Transaction(product, date.today()))
                self.clients[newClient] = Transaction(product, date.today())
                list_of_clients.append(newClient)
                print("Transakacja się powiodła.")
            else:
                print("Transakcja się nie powiodła.")
        else:
            purchased_products = found_client.buy(product, amount)
            if purchased_products:
                self.clients[found_client] = Transaction(product, date.today())
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
            if any(part.isdigit() for part in client_name.split(" ")):
                print("Nazwa klienta powinna być napisem.")
                return

            purchased_services = newClient.buy_service(service)
            if purchased_services:
                self.transactions.append(Transaction(service, date.today()))
                self.clients[newClient] = Transaction(service, date.today())
                list_of_clients.append(newClient)
                print("Transakacja się powiodła.")
            else:
                print("Transakcja się nie powiodła.")
        else:
            purchased_services = found_client.buy_service(service)
            if purchased_services:
                self.clients[found_client] = Transaction(service, date.today())
                print("Transakcja się powiodła.")
            else:
                print("Transakcja się nie powiodła.")

    def __str__(self):
        return f"""
{self.clients[client]}
{self.client}"""


if __name__ == "__main__":

    product_json = "products.json"  # Ścieżka do pliku JSON (produkty)
    service_json = "services.json"  # Ścieżka do pliku JSON (uslugi)
    client = Client("Szymon", "Szkarłat")
    clients = {client: []}
    list_of_clients = [client for client in clients]
    store = Store(clients, product_json, service_json)
    # for client in clients:
    # print(client)
    # print(list_of_clients)
    # print(store.clients[Client("Szymon", "Szkarłat")])
    # for client in clients:
    #     print(clients[client])

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
                    # difference = int(inputDataList[1]) - first_number_id

                    print(store.clients[Client(inputDataList[1], inputDataList[2])], end="")
                    # print(client)
                    for client in store.clients:
                        if client.__eq__(Client(inputDataList[1], inputDataList[2])):
                            print(client)
                except:
                    for clientTransactions in store.clients:
                        print(clientTransactions)
                    # for i in list_of_clients:
                    #     print(i)
                    # print(store.)
                # except:
                #     print("Niepoprawna komenda!")
                # except:
                #     print("WSZYSTKIE TRANSAKCJE!!!")
                #     print("-----------------------")
                #     for transaction in store.transactions:
                #         print(transaction) 
                    
            elif inputDataList[0] == "sell":
                print(inputDataList)
                try:
                    if inputDataList[1] == "product":
                        store.sell_product_to_client(inputDataList[2], inputDataList[3], int(inputDataList[4]), int(inputDataList[5]))
                    elif inputDataList[1] == "service":
                        store.sell_service_to_client(inputDataList[2], inputDataList[3], int(inputDataList[4]))
                except (IndexError, ValueError):
                    print("Niepoprawna komenda!")
                    # if not list_of_clients:
                    #     if int(inputDataList[1]) < 0:
                    #         print("Id musi iść być liczba naturalną")
                    #     else:
                    #         first_number_id = int(inputDataList[1])
                    #         Client.next_id = first_number_id
                    #         store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                    # else:
                    #     if int(inputDataList[1]) - Client.next_id == 0:
                    #         store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                    #     elif first_number_id <= int(inputDataList[1]) <= Client.next_id - 1:
                    #         store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                    #     else:
                    #         print("Id musi iść po kolei.")
                    #         print("Kolejne id: ", Client.next_id)
                       
                except (IndexError, ValueError):
                    print("Niepoprawna komenda!")                
            else:
                print("Nieznana komenda!")
    except EOFError:
        exit()

    def __str__(self):
        return f"""
{self.clients[client]}
{self.client}"""


if __name__ == "__main__":

    product_json = "products.json"  # Ścieżka do pliku JSON (produkty)
    service_json = "services.json"  # Ścieżka do pliku JSON (uslugi)
    client = Client("Szymon", "Szkarłat")
    clients = {client: []}
    list_of_clients = [client for client in clients]
    store = Store(clients, product_json, service_json)
    # for client in clients:
    # print(client)
    # print(list_of_clients)
    # print(store.clients[Client("Szymon", "Szkarłat")])
    # for client in clients:
    #     print(clients[client])

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
                # try:
                    # difference = int(inputDataList[1]) - first_number_id

                    print(store.clients[Client(inputDataList[1], inputDataList[2])], end="")
                    # print(client)
                    for client in store.clients:
                        if client.__eq__(Client(inputDataList[1], inputDataList[2])):
                            print(client)
                    # for i in list_of_clients:
                    #     print(i)
                    # print(store.)
                # except:
                #     print("Niepoprawna komenda!")
                # except:
                #     print("WSZYSTKIE TRANSAKCJE!!!")
                #     print("-----------------------")
                #     for transaction in store.transactions:
                #         print(transaction) 
                    
            elif inputDataList[0] == "sell":
                print(inputDataList)
                try:
                    if inputDataList[1] == "product":
                        store.sell_to_client(inputDataList[2], inputDataList[3], int(inputDataList[4]), int(inputDataList[5]))
                    elif inputDataList[1] == "service":
                        store.sell_to_client(inputDataList[2], inputDataList[3], int(inputDataList[4]))
                    # if not list_of_clients:
                    #     if int(inputDataList[1]) < 0:
                    #         print("Id musi iść być liczba naturalną")
                    #     else:
                    #         first_number_id = int(inputDataList[1])
                    #         Client.next_id = first_number_id
                    #         store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                    # else:
                    #     if int(inputDataList[1]) - Client.next_id == 0:
                    #         store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                    #     elif first_number_id <= int(inputDataList[1]) <= Client.next_id - 1:
                    #         store.sell_to_client(int(inputDataList[1]), int(inputDataList[2]), int(inputDataList[3]))
                    #     else:
                    #         print("Id musi iść po kolei.")
                    #         print("Kolejne id: ", Client.next_id)
                       
                except (IndexError, ValueError):
                    print("Niepoprawna komenda!")                
            else:
                print("Nieznana komenda!")
    except EOFError:
        exit()