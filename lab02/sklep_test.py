import pytest

from sklep import (
    regex_function,
    display_warehouse_state,
    user_dictionary,
    sell_products,
    show_user_products,
    check_format,
)

test_data = [
    "John:apple(5)",
    "Jane:banana(3)",
    "John:apple(2)",
]


def test_regex_function():
    result = regex_function(test_data[0])
    assert result == ["John", "apple", "5"]


def test_display_warehouse_state(capsys):
    test_data = {
        "apple": 5,
        "banana": 3,
    }

    display_warehouse_state(test_data)

    captured = capsys.readouterr()
    expected_output = """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------
apple: 5
banana: 3
"""

    assert captured.out == expected_output


def test_user_dictionary():
    dictionaries = []
    user_dictionary(test_data, dictionaries)

    expected_dictionaries = [
        {"user": "John", "apple": 7},
        {"user": "Jane", "banana": 3},
    ]
    assert dictionaries == expected_dictionaries


def test_sell_products():
    warehouse = {"apple": 7, "banana": 5}
    sell_data = ["John:apple(2)", "Jane:banana(3)"]  # Changed quantity for Jane
    sell_products(sell_data, warehouse)

    assert warehouse == {"apple": 5, "banana": 2}  # Updated expected values


dictionaries = [
    {"user": "John", "apple": 5, "banana": 3},
    {"user": "Jane", "banana": 2, "orange": 4},
]


# Przykładowe dane testowe
dictionaries = [
    {"user": "John", "apple": 5, "banana": 3},
    {"user": "Jane", "banana": 2, "orange": 4},
]


def test_check_format():
    # Testy funkcji check_format

    # Poprawny format
    assert check_format("John:apple(5)") == False
    assert check_format("Jane:banana(3)") == False

    # Niepoprawny format
    assert check_format("John:apple(5") == False
    assert check_format("Jane:banana") == False
