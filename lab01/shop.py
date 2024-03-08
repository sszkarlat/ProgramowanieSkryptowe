import sys

warehouse = {"Komputer": 10, "Laptop": 20}


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


def show_warehouse_status(warehouse):
    print(
        """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------"""
    )
    for product, amountOfProduct in warehouse.items():
        print(f"{product}   {amountOfProduct}")


if __name__ == "__main__":
    if sys.argv[-1] == "--show_status":
        wishList = sys.argv[1:-1]
        warehouse = sell_product(warehouse, wishList)
        show_warehouse_status(warehouse)
    else:
        wishList = sys.argv[1:]
        warehouse = sell_product(warehouse, wishList)
