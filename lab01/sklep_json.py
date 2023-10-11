import sys
import json

nazwaPliku = "magazyn.json"


def wczytaj_magazyn(nazwaPliku):
    with open(nazwaPliku, "r") as plik:
        return json.load(plik)


magazyn = wczytaj_magazyn(nazwaPliku)


def zapisz_magazyn(nazwaPliku, magazyn):
    with open(nazwaPliku, "w") as plik:
        json.dump(magazyn, plik)


def sprzedaz_towaru(magazyn, listaZyczen):
    for i in range(0, len(listaZyczen), 2):
        produkt = listaZyczen[i]
        ilosc = int(listaZyczen[i + 1])

        if produkt in magazyn:
            if ilosc >= 0:
                if ilosc <= magazyn[produkt]:
                    magazyn[produkt] -= ilosc
                else:
                    print(f"W magazynie nie ma tylu sztuk produktu: {produkt}.")
            else:
                print(f"Nie można kupić ujemnej liczby sztuk produktu: {produkt}.")
        else:
            print(f"Produktu: {produkt} nie ma w magazynie.")
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
    if sys.argv[-1] == "--stan_sklepu":
        listaZyczen = sys.argv[1:-1]
        magazyn = sprzedaz_towaru(magazyn, listaZyczen)
        stan_sklepu(magazyn)
        zapisz_magazyn(nazwaPliku, magazyn)
