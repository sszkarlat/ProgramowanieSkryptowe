import re
from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument("file", help="filename")
args = arg_parser.parse_args()
# print(args)

file = args.file


def regex_function(inputData):
    Regex = re.compile(r"\w*[^\s:\(\)]")
    return Regex.findall(inputData)


def load_input_data(file):
    with open(file, "r") as f:
        warehouse = f.read().splitlines()
    warehouseDict = {
        warehouse[i]: int(warehouse[i + 1]) for i in range(0, len(warehouse), 2)
    }
    return warehouseDict


def display_warehouse_state(warehouseDict):
    print(
        """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------"""
    )
    for product, amountOfProduct in warehouseDict.items():
        print(f"{product}: {amountOfProduct}")


def user_dictionary(inputData, dictionaries):
    for data in inputData:
        dataList = regex_function(data)
        user_name = dataList[0]

        # Sprawdź, czy użytkownik już istnieje w słownikach
        user_exists = False
        for dictionary in dictionaries:
            if dictionary["user"] == user_name:
                user_exists = True
                break

        if not user_exists:
            newDictionary = {"user": user_name}
            for i in range(1, len(dataList), 2):
                newDictionary[dataList[i]] = int(dataList[i + 1])
            dictionaries.append(newDictionary)
        else:
            for dictionary in dictionaries:
                if dictionary["user"] == user_name:
                    for i in range(1, len(dataList), 2):
                        if dataList[i] in dictionary:
                            dictionary[dataList[i]] += int(dataList[i + 1])
                        else:
                            dictionary[dataList[i]] = int(dataList[i + 1])


def sell_products(inputData, warehouseDict):
    # print(inputData)
    for data in inputData:
        dataList = regex_function(data)

        dictionary = {}
        for i in range(1, len(dataList), 2):
            dictionary[dataList[i]] = int(dataList[i + 1])

        for product in dictionary:
            amountOfProduct = dictionary[product]
            if product in warehouseDict.keys():
                if amountOfProduct >= 0:
                    if amountOfProduct <= warehouseDict[product]:
                        warehouseDict[product] -= amountOfProduct
                    else:
                        print(
                            f"Towaru: {product} jest tylko {warehouseDict[product]} sztuk"
                        )
                else:
                    print(f"Nie można wybrać ujemnej liczby towaru: {product}")
            else:
                print(f"{product} - nie ma takiego towaru")


def show_user_products(users):
    for user in users:
        for dictionary in dictionaries:
            if dictionary["user"] == user:
                filteredDictionary = {
                    key: value for key, value in dictionary.items() if key != "user"
                }

                print(user)
                print(
                    """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------"""
                )
                for product, amountOfProduct in filteredDictionary.items():
                    print(f"{product}: {amountOfProduct}")
        print("")


def check_format(text):
    checkRegex = re.compile(r"\w*_\w*(:\w+\(\d\))+")
    return bool(checkRegex.search(text))


dictionaries = []

if __name__ == "__main__":
    try:
        warehouseDict = load_input_data(file)
        try:
            while True:
                inputDataList = (input("> ")).split(" ")
                # print(inputDataList)
                if inputDataList[0] == "warehouse":
                    display_warehouse_state(warehouseDict)
                elif inputDataList[0] == "sell":
                    for i in range(1, len(inputDataList)):
                        if check_format(inputDataList[i]):
                            flag = True
                        else:
                            print("Niepoprawny format komendy")
                            flag = False
                    if flag == True:
                        sell_products(inputDataList[1:], warehouseDict)
                        user_dictionary(inputDataList[1:], dictionaries)
                    else:
                        continue
                    print(dictionaries)
                elif inputDataList[0] == "show":
                    show_user_products(inputDataList[1::2])
                    # print(inputDataList[1::2])
                else:
                    print("Nieznana komenda")

        except EOFError:
            exit()
    except FileNotFoundError:
        print("Nieprawidłowa nazwa pliku!")
