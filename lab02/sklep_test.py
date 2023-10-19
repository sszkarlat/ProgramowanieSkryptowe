import re
from sklep import (
    regex_function,
    load_input_data,
    add_to_dictionary,
    sell_products,
    check_format,
    display_warehouse_state,
    user_dictionary,
    show_user_products,
)


def test_regex_function():
    input_data = "abc:1 def(2) ghi:3"
    expected_output = ["abc", "def", "ghi"]
    assert regex_function(input_data) == expected_output


def test_load_input_data():
    file_contents = "product1\n10\nproduct2\n5"
    with open("test_file.txt", "w") as test_file:
        test_file.write(file_contents)

    expected_output = {"product1": 10, "product2": 5}
    assert load_input_data("test_file.txt") == expected_output

    import os

    os.remove("test_file.txt")


def test_add_to_dictionary():
    input_data = ["_category1", "item1", "item2", "_category2", "item3"]
    expected_output = {"_category1": ["item1", "item2"], "_category2": ["item3"]}
    assert add_to_dictionary(input_data) == expected_output


def test_sell_products():
    warehouse_dict = {"product1": 10, "product2": 5}
    input_data = ["user1:product1(2) product2(3)"]
    sell_products(input_data, warehouse_dict)
    expected_output = {"product1": 8, "product2": 2}
    assert warehouse_dict == expected_output


def test_check_format():
    valid_input = "abc:def(1)"
    invalid_input = "abc:def(1"
    assert check_format(valid_input) == True
    assert check_format(invalid_input) == False


def test_display_warehouse_state():
    warehouse_dict = {"product1": 10, "product2": 5}
    expected_output = """-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------
product1: 10
product2: 5
"""
    result = display_warehouse_state(warehouse_dict)
    assert result == expected_output


def test_user_dictionary():
    user_data = ["user1:product1(2) product2(3)"]
    user_dicts = []
    user_dictionary(user_data, user_dicts)
    expected_output = [{"user": "user1", "product1": 2, "product2": 3}]
    assert user_dicts == expected_output


def test_show_user_products():
    user_dicts = [{"user": "user1", "product1": 2, "product2": 3}]
    # We will use capture output to check the printed content
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output
    show_user_products(["user1"], user_dicts)
    sys.stdout = sys.__stdout__

    expected_output = """user1
-------------+------------
Nazwa towaru | Ilość sztuk
-------------+------------
product1: 2
product2: 3
"""
    assert captured_output.getvalue() == expected_output
