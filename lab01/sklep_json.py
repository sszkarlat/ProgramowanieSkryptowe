import sys
import json


# Funkcja do wczytywania magazynu z pliku JSON
def wczytaj_magazyn(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return {}


# Funkcja do zapisywania magazynu do pliku JSON
def zapisz_magazyn(nazwa_pliku, magazyn):
    with open(nazwa_pliku, "w") as plik:
        json.dump(magazyn, plik)


# Pobierz nazwę pliku JSON z argumentów wiersza poleceń
if len(sys.argv) < 2:
    print("Podaj nazwę pliku JSON z magazynem.")
    sys.exit(1)

nazwa_pliku = sys.argv[1]

# Wczytaj magazyn z pliku JSON
magazyn = wczytaj_magazyn(nazwa_pliku)


def sprzedaz_towaru(magazyn):
    lista = sys.argv[2:-1]
    nowy_magazyn = magazyn.copy()

    for i in range(0, len(lista), 2):
        produkt = lista[i]
        ilosc = int(lista[i + 1])

        if produkt in magazyn:
            if isinstance(ilosc, int) and ilosc > 0:
                if produkt in nowy_magazyn:
                    nowy_magazyn[produkt] -= ilosc
                else:
                    print(f"Produkt {produkt} nie istnieje w magazynie.")
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
        magazyn = sprzedaz_towaru(magazyn)
        stan_sklepu(magazyn)
        # Zapisz zmodyfikowany magazyn do pliku JSON
        zapisz_magazyn(nazwa_pliku, magazyn)
