# Laboratorium 1. :star2:
Najważniejszym elementem tegoż laboratorium jest **obsługa plików w formacie JSON**. Ponadto istotny element stanowi obsługa danych wprowadzanych przez użytownika do [**CLI**](https://www.youtube.com/watch?v=QJBVjBq4c7E) (ang. _Command Line_ - wiersza poleceń).

# Co, gdzie jest?
## shop.py :shopping:
Jest to uproszczona wersja Magazyn (ang. _warehouse_) jest na stałe zdefiniowany (ang. _hard-coded_). W pliku tym mamy jedynie zdefiniowaną główną i najważniejszą funckję (sell_product), która odpowiada za sprzedaż w odpowiedniej ilości poroduktów, na podstawie danych, które klient wprowadził do CLI.

## shop_json.py :open_file_folder:
W tym pliku mamy dla odmiany dane wczytywane z pliku w formacie JSON. Po dokonaniu zakupu, dane są również zapisywane są do pliku warehouse.json.

## warehouse.json :chart_with_downwards_trend:
Plik w formacie [JSON](https://kamil.kwapisz.pl/json-xml/).