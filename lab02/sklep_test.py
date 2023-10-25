import pytest

from sklep import (
    regex_function,
    display_warehouse_state,
    user_dictionary,
    sell_products,
    check_format,
    load_input_data,
)

test_data = [
    "Jan_Kowalski:Laptop(2)",
    "Anna_Dymna:Komputer(3)",
    "Jerzy_Janowiczn:Laptop(1)",
]


def test_regex_function():
    result = regex_function(test_data[0])
    assert result == ["Jan_Kowalski", "Laptop", "2"]


def test_display_warehouse_state(capsys):
    test_data = {
        "Komputer": 5,
        "Laptop": 3,
    }

    display_warehouse_state(test_data)

    captured = capsys.readouterr()
    expected_output = """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------
Komputer: 5
Laptop: 3
"""

    assert captured.out == expected_output


def test_sell_products():
    warehouse = {"Komputer": 5, "Laptop": 3}
    sell_data = [
        "Jan_Kowalski:Komputer(2)",
        "Anna_Dymna:Laptop(3)",
    ]
    sell_products(sell_data, warehouse)

    assert warehouse == {"Komputer": 3, "Laptop": 0}


def test_check_format():

    assert check_format("Jan_Kowalski:Komputer(5)") is True
    assert check_format("Anna_Dymna:Laptop(3)") is True

    assert check_format("Jan:apple(5") is False
    assert check_format("Anna_Dymna:Komputer") is False
