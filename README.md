# Programowanie skryptowe 😎
Repozytorium to zawiera kod, który wyprodukowałem podczas zajęć laboratoryjnych z przedmiotu Programowanie Skryptowe. Głównie jest to Python, JS, HTML & CSS. Polecam zajrzeć również do podlinkowanych stron czy treści wideo. Miłej lektury! :wink:

# Co, gdzie jest?
## Zanim zaczniesz, kilka artykułów :open_book:
- [początkujący programista i jego błędy](https://bulldogjob.pl/readme/poczatkujacy-programista-i-jego-bledy)
- [jak używać Flexboxa w CSS (przykłady)](https://bulldogjob.pl/readme/jak-uzywac-flexbox-w-css-przyklady)
- [dobry programista](https://bulldogjob.pl/readme/dobry-programista-czym-sie-wyroznia)
- [Co po studiach informatycznych?](https://bulldogjob.pl/readme/co-po-studiach-informatycznych)
- [Wzloty i upadki - historia JavaScripta](https://bulldogjob.pl/readme/wzloty-i-upadki-historia-javascript)
- Więcej ciekawych artykułów i treści - [czytaj dalej](https://bulldogjob.pl/readme)


## Zadania :house:
### 1. Podstawy języka Python: :nerd_face:
- jakie typowanie oferuje Python: [słabe](https://pl.wikipedia.org/wiki/Typowanie_s%C5%82abe), [silne](), [statyczne](https://pl.wikipedia.org/wiki/Typowanie_statyczne) czy [dynamiczne](https://pl.wikipedia.org/wiki/Typowanie_dynamiczne)
- [funkcje](https://www.programiz.com/python-programming/function) w Python
- przekazywanie argumentów wiersza poleceń - [artykuł](https://docs.python.org/3/library/sys.html#sys.argv)
- słownik w Python - [jak działa](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) 
- Testy jednostkowe:
    * [porównanie frameworków służących do automatyzacji testów](https://bulldogjob.pl/readme/pytest-vs-unittest-porownanie-frameworkow-do-automatyzacji-testow-w-pythonie) 
    * [jak złapać to co wyrzuca nam wyjście](https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html)
    * sprawdzanie stdin (standardowego wejścia), stdout (standardowego wyjścia), stderr (strumień błędów) w Python przy pomocy [testów jednostkowych](https://ryip.me/posts/python/unittest-stdout-stderr/)
    * konfiguracja [testów w VisualStudioCode](https://ryip.me/posts/python/unittest-stdout-stderr/)
- tworzenie dokumentacji w Python:
    * [Python DocStrings](https://www.youtube.com/watch?v=0YUdYk5E-w4)
    * [Auto DocString Extension in VSC](https://www.youtube.com/watch?v=2xa9_A8HH3U)
    * utworzenie dokumentacji w [formacie HTML](https://qabrio.pl/sphinx-generacja-specyfikacji/) oraz jako dodatkowa pomoc[filmik na YouTube](https://www.youtube.com/watch?v=BWIrhgCAae0)
- przetwarzanie danych a linia komend, przy wykorzystaniu metod klasy, odpowiednio:
    * [list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
    * [dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
    * [set](https://docs.python.org/3/tutorial/datastructures.html#sets)

### 2. Zabawa na łańcuchach znaków (string): :partying_face:
- Podstawowe operacje na tekście:
    * w Python skrypty łatwiej i częściej tworzy się przy użyciu techniki Code & Fix (Najpierw coś piszemy/kodujemy, a dopiero później debugujemy i poprawiamy ewentualne błędy). Rzadziej robi się to przy pomocy techniki [Test Driven Development](https://softnauts.com/pl/blog/tdd-co-to-jest-i-dlaczego-warto-go-uzywac), gdzie najpierw piszemy testy jednostkowe, a dopiero później, na ich podstawie uzupełniamy funkcje. [Przykład](https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/)
    * [metody klasy 'string'](http://www.oprojektowaniu.pl/python-dla-inzynierow-napisy/) (indeksowanie, wycinkowanie, łączenie oraz powielanie)
- włsne moduły, import from, as: [filmik na YT](https://www.youtube.com/watch?v=EFIX33Mjzpg)
- samouczek programisty TDD (Test Driven Development) na [przykładzie](https://www.samouczekprogramisty.pl/test-driven-development-na-przykladzie/)
- procedury tworzenia TDD:
    * napisać test
    * napisać tylko tyle kodu, aby ten test został spełniony
    * [sfaktoryzować kod](https://infotraining.bitbucket.io/cpp-tdd/tdd.htm) do najprostszej implementacji funkcjonalności określonej przez test
    * poprawa ewentualnych błędów i dalsza faktoryzacja
- Python vs C:
    * funkcje biblioteczne do [obsługi napisów](https://www.gnu.org/software/libc/manual/html_node/String-and-Array-Utilities.html) oraz [wyrażeń regularnych](https://www.gnu.org/software/libc/manual/html_node/Pattern-Matching.html)
    * usługi [przetwarzania tekstu w Python](https://docs.python.org/pl/3/library/text.html)
- zaawansowane obsługi linii komend (CLI - Command Line):
    * [parsery](https://newsblog.pl/jak-analizowac-argumenty-wiersza-polecen-w-pythonie/) (tzw. parsowanie (analizowanie) linii komend)
    * do obsługi linii komend używa się modułu/parsera [argparse](https://docs.python.org/pl/3/library/argparse.html) (zalecany) lub [getopt](https://docs.python.org/pl/3/library/getopt.html) (na wzór używanej w C funkcji [getopt()](https://en.wikipedia.org/wiki/Getopt))
    * Parser argparse generuje angielskojęzyczną wersje pomocy. Możliwe jest [wygenerowanie wersji polskojęzycznej poprzez tłumaczenie komunikatów](https://stackoverflow.com/questions/22951442/how-to-make-pythons-argparse-generate-non-english-text) 

### 2. Klasy oraz enumy: :coffee:
- Rodzaje metod klas:
    * programowanie obiektowe | Metody specjalne [film na YT](https://www.youtube.com/watch?v=KgP_9A_x-Qo)
    * w artykule [__init__ Vs __new__ Methods In Python](https://geekpython.in/init-vs-new) – With Examples wyjaśniono, jak działają te metody
- hermetyzacja:
    * [akcesory i mutatory](https://www.slawomirkwiatkowski.pl/index.php/2019/09/08/akcesory-i-mutatory-w-pythonie-cz-1/) w Python
    * Wyzwanie Python: [„Programowanie obiektowe”](https://www.kodolamacz.pl/blog/wyzwanie-python-4-programowanie-obiektowe/) & [YT] (https://www.youtube.com/watch?v=qDDUTDMljvk)
    * sprawdzanie typu argumentu za pomocą funkcji [isinstance()](https://www.programiz.com/python-programming/methods/built-in/isinstance)
- tworzenie typu wyliczeniowego, [dokumentacja](https://docs.python.org/3/library/enum.html) 


## Laboratoria :computer:
1. 