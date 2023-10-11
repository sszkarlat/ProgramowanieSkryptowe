import sys

magazyn = {"Komputer": 10, "Laptop": 20}


def sprzedaz_towaru(magazyn):
    lista = sys.argv[1:-1]
    nowy_magazyn = {}

    for i in range(0, len(lista), 2):
        produkt = lista[i]
        ilosc = int(lista[i + 1])

        if produkt in magazyn:
            if isinstance(ilosc, int) and ilosc > 0:
                if produkt in nowy_magazyn:
                    nowy_magazyn[produkt] += ilosc
                else:
                    nowy_magazyn[produkt] = ilosc
            else:
                print(f"Ilość produktu {produkt} nie jest liczbą całkowitą: {ilosc}")
        else:
            print(f"Produkt {produkt} nie istnieje w magazynie.")

    for produkt, ilosc in nowy_magazyn.items():
        if ilosc <= magazyn[produkt]:
            magazyn[produkt] -= ilosc
        else:
            print(f"Nie ma tyle sztuk produktu: {produkt}")
    return magazyn


def stan_sklepu(magazyn):
    print(
        """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------"""
    )
    for produkt, ilosc in magazyn.items():
        print(f"{produkt}   {ilosc}")


if __name__ == "__main__":
    if sys.argv[-1] == "--stan_magazynu":
        sprzedaz_towaru(magazyn)
        stan_sklepu(magazyn)
