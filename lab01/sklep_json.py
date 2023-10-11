import sys
import json

nazwa_pliku = "magazyn.json"


def wczytaj_magazyn(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        return json.load(plik)


def zapisz_magazyn(nazwa_pliku, magazyn):
    with open(nazwa_pliku, "w") as plik:
        json.dump(magazyn, plik)


magazyn = wczytaj_magazyn(nazwa_pliku)


def sprzedaz_towaru(magazyn, lista_sprzedazy):
    nowy_magazyn = magazyn.copy()

    for i in range(0, len(lista_sprzedazy), 2):
        produkt = lista_sprzedazy[i]
        ilosc = int(lista_sprzedazy[i + 1])

        if produkt in nowy_magazyn:
            if ilosc <= nowy_magazyn[produkt]:
                if ilosc > 0:
                    nowy_magazyn[produkt] -= ilosc
                else:
                    print(f"Nie możesz kupić ujemnej liczby sztuk produktu: {produkt}")
            else:
                print(f"Nie ma tylu sztuk produktu: {produkt} w magazynie")
        else:
            print(f"Produkt: {produkt} nie istnieje w magazynie.")
    return nowy_magazyn


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
        lista_sprzedazy_sprzedazy = sys.argv[1:-1]
        magazyn = sprzedaz_towaru(magazyn, lista_sprzedazy_sprzedazy)
        stan_sklepu(magazyn)
        zapisz_magazyn(nazwa_pliku, magazyn)
