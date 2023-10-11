import sys

magazyn = {"Komputer": 10, "Laptop": 20}


def sprzedaz_towaru(magazyn, listaZyczen):
    nowyMagazyn = magazyn.copy()

    for i in range(0, len(listaZyczen), 2):
        produkt = listaZyczen[i]
        ilosc = int(listaZyczen[i + 1])

        if produkt in nowyMagazyn:
            if ilosc >= 0:
                if ilosc <= nowyMagazyn[produkt]:
                    nowyMagazyn[produkt] -= ilosc
                else:
                    print(f"W magazynie nie ma tylu sztuk produktu: {produkt}.")
            else:
                print(f"Nie można kupić ujemnej liczby sztuk produktu: {produkt}.")
        else:
            print(f"Produktu: {produkt} nie ma w magazynie.")
    return nowyMagazyn


def stan_sklepu(magazyn):
    print(
        """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------"""
    )
    for produkt, ilosc in magazyn.items():
        print(f"{produkt}   {ilosc}")


if __name__ == "__main__":
    if sys.argv[-1] == "--stan_sklepu":
        listaZyczen = sys.argv[1:-1]
        nowyMagazyn = sprzedaz_towaru(magazyn, listaZyczen)
        stan_sklepu(nowyMagazyn)
