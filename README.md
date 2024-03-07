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
- zaawansowana obsługa linii komend (CLI - Command Line):
    * [parsery](https://newsblog.pl/jak-analizowac-argumenty-wiersza-polecen-w-pythonie/) (tzw. parsowanie (analizowanie) linii komend)
    * do obsługi linii komend używa się modułu/parsera [argparse](https://docs.python.org/pl/3/library/argparse.html) (zalecany) lub [getopt](https://docs.python.org/pl/3/library/getopt.html) (na wzór używanej w C funkcji [getopt()](https://en.wikipedia.org/wiki/Getopt))
    * Parser argparse generuje angielskojęzyczną wersje pomocy. Możliwe jest [wygenerowanie wersji polskojęzycznej poprzez tłumaczenie komunikatów](https://stackoverflow.com/questions/22951442/how-to-make-pythons-argparse-generate-non-english-text) 

### 3. Klasy oraz enumy: :coffee:
- Rodzaje metod klas:
    * programowanie obiektowe | Metody specjalne [film na YT](https://www.youtube.com/watch?v=KgP_9A_x-Qo)
    * w artykule [_/__init__ Vs __new__ Methods In Python_](https://geekpython.in/init-vs-new) – With Examples wyjaśniono, jak działają te metody
- hermetyzacja:
    * [akcesory i mutatory](https://www.slawomirkwiatkowski.pl/index.php/2019/09/08/akcesory-i-mutatory-w-pythonie-cz-1/) w Python
    * Wyzwanie Python: [_„Programowanie obiektowe”_](https://www.kodolamacz.pl/blog/wyzwanie-python-4-programowanie-obiektowe/) & [YT](https://www.youtube.com/watch?v=qDDUTDMljvk)
    * sprawdzanie typu argumentu za pomocą funkcji [isinstance()](https://www.programiz.com/python-programming/methods/built-in/isinstance)
- tworzenie typu wyliczeniowego, [dokumentacja](https://docs.python.org/3/library/enum.html)

### 4. Interakcja między obiektami: :electric_plug:
- Type [hints](https://docs.python.org/pl/3/library/typing.html) & [film na YT](https://www.youtube.com/watch?v=WoasJKaAvaI)
- Enum z metodami:
    * Python’s self type: _“How to annotate methods that return self”_ [article](https://realpython.com/python-type-self/)
    * nowe [typy wyliczeniowe](https://www.golinuxcloud.com/python-enum/)
- kompozycja:
    * Python obiektowy - [kompozycja](https://www.youtube.com/watch?v=C4nOLhfq7L4)
    * Jak używać i odnotowywać domyślne argumenty w funkcjach Python? [artykuł](https://pl.from-locals.com/python-argument-default/)
    * [zasada DRY](https://boringowl.io/blog/zasada-dry-w-programowaniu-strategie-sprzyjajace-optymalizacji-i-poprawie-jakosci-kodu) - z ang. _"Don't Repeat Yourself"_ -_"Nie powtarzaj się"_ - reguła zalecająca unikanie powtarzania tego samego fragmentu kodu.
    * [kurs TDD część 2](https://dariuszwozniak.net/posts/kurs-tdd-2-testy-jednostkowe-a-testy-integracyjne/) - testy jednostkowe a testy integracyjne; jakie są podstawowe różnice
- tworzenie symulacji:
    * Python [hash](https://www.pythontutorial.net/python-oop/python-__hash__/)

### 5. Klasy abstrakcyjne a dziedziczenie :bricks:
- przekształcenie modułu _model_ w pakiet:
    * w przypadku skomplikowanych projektów tworzy się [pakiety](https://docs.python.org/pl/3/tutorial/modules.html#packages), [pakiety przestrzeni nazw](https://realpython.com/python-namespace-package/)
    * [import bezwzględny](https://realpython.com/absolute-vs-relative-python-imports/#absolute-imports)
    * [import względny](https://realpython.com/absolute-vs-relative-python-imports/#relative-imports)
    * zmienna środowiskowa [PYTHONPATH](https://note.nkmk.me/en/python-import-module-search-path/#add-new-module-search-path-with-pythonpath)
- [klasy abstrakcyjne](https://oscarsierraproject.eu/artykuly/czytaj/python-klasy-abstrakcyjne-i-interfejsy)
- [_"How to rename a dictionary key in Python"_](https://www.adamsmith.haus/python/answers/how-to-rename-a-dictionary-key-in-python)
- [_"Python for else"_](https://www.w3schools.com/python/gloss_python_for_else.asp)
- dziedziczenie (ang. _inheritance_):
    * [_"Method overriding in Python"_](https://www.thedigitalcatonline.com/blog/2014/05/19/method-overriding-in-python/)
    * [metoda super()](https://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad8.html#metody_bazowe)
    * [polimorfizm](https://www.kodolamacz.pl/blog/wyzwanie-python-5-zaawansowane-aspekty-programowania-obiektowego/#polimorfizm) - co to takiego?
- [dziedziczenie vs kompozycja](https://helion.pl/blog/dziedziczenie-vs-kompozycja-20) (ang. _inheritance vs composition_) & [_"Kompozycja ponad dziedziczenie"_](https://sarvendev.com/2017/10/kompozycja-ponad-dziedziczenie/)
- [wzorca projektowe](https://refactoring.guru/pl/design-patterns) poświęcone programowaniu obiektowemu ([Python]( https://refactoring.guru/pl/design-patterns/python)) wzorzec architektoniczny - [Model-Widok-Kontroler](https://pl.wikipedia.org/wiki/Model-View-Controller)

### 6. Wyjątki, dekoratory oraz programowanie funkcyjne :snake:
- Wyjątek [_Value Error_](https://docs.python.org/pl/3/library/exceptions.html#ValueError)
- [Tworzenie własnej klasy wyjątku](https://www.geeksforgeeks.org/user-defined-exceptions-python-examples/)
- Dekoratory (ang. _decorators_):
    * [film na YT](https://www.youtube.com/watch?v=7fIpdbEtqW4)
    * [lecture](https://www.icsr.agh.edu.pl/~polak/wyklady/jezyki/skryptowe.pdf#page=36)
    * [desc1](https://analityk.edu.pl/python-dekoratory/)
    * [desc2](https://chyla.org/artykuly/python/python-dekoratory.html)
    * [kwalifikowana nazwa](https://docs.python.org/pl/3/library/stdtypes.html#definition.__qualname__)
- Programowanie funkcyjne:
    * [film na YT](https://www.youtube.com/watch?v=cmiMEzu_5Ng)
    * [lecture](https://www.icsr.agh.edu.pl/~polak/wyklady/jezyki/skryptowe.pdf#page=39)
    * [desc1](https://www.dobreprogramy.pl/iluzion/Programowanie-funkcyjne-w-Pythonie,25498.html )
    * [desc2](https://stackabuse.com/functional-programming-in-python/ )
    * [desc3](https://docs.python.org/pl/3/howto/functional.html )


## Laboratoria :computer:
1. 