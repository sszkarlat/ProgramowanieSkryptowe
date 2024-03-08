import sys
import json

fileName = "warehouse.json"


# Load data into a file (warehouse.json)
def load_warehouse(fileName):
    with open(fileName, "r") as file:
        return json.load(file)


# The warehouse is loaded from the file
warehouse = load_warehouse(fileName)


# Save current warehouse status to the file
def save_warehouse(fileName, warehouse):
    with open(fileName, "w") as file:
        json.dump(warehouse, file)


# Sell ​​products ordered by customer on Command Line
def sell_product(warehouse, wishList):
    for i in range(0, len(wishList), 2):
        product = wishList[i]
        amountOfProduct = int(wishList[i + 1])

        if product in warehouse:
            if amountOfProduct >= 0:
                if amountOfProduct <= warehouse[product]:
                    warehouse[product] -= amountOfProduct
                    print(f"Kupiono produkt: {
                          product}, w ilości {amountOfProduct}")
                else:
                    print(
                        f"W magazynie nie ma tylu sztuk produktu: {product}.")
            else:
                print(
                    f"Nie można kupić ujemnej liczby sztuk produktu: {product}.")
        else:
            print(f"Produktu: {product} nie ma w magazynie.")
    return warehouse


# Show current warehouse status
def show_warehouse_status(warehouse):
    print(
        """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------"""
    )
    for product, amountOfProduct in warehouse.items():
        print(f"{product}   {amountOfProduct}")


if __name__ == "__main__":
    if sys.argv[-1] == "--show-status":
        wishList = sys.argv[1:-1]
        warehouse = sell_product(warehouse, wishList)
        show_warehouse_status(warehouse)
        save_warehouse(fileName, warehouse)
    else:
        wishList = sys.argv[1:]
        warehouse = sell_product(warehouse, wishList)
        save_warehouse(fileName, warehouse)
