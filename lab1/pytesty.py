import sys
import pytest
from skrypt import display, run, moves_description


# Testy dla funkcji display
def test_display_without_index(capsys):
    args = ["arg1", "arg2", "arg3"]
    display(args, False)
    out, err = capsys.readouterr()
    assert out == "Start\narg1\narg2\narg3\nStop\n"


def test_display_with_index(capsys):
    args = ["arg1", "arg2", "arg3"]
    display(args, True)
    out, err = capsys.readouterr()
    assert out == "Start\nargs[0] = arg1\nargs[1] = arg2\nargs[2] = arg3\nStop\n"


# Testy dla funkcji run
def test_run():
    moves = ["f", "b", "l", "r", "x"]
    expected_result = [
        "Zwierzak idzie do przodu",
        "Zwierzak idzie do tyłu",
        "Zwierzak skręca w lewo",
        "Zwierzak skręca w prawo",
    ]
    assert run(moves, moves_description) == expected_result


def test_run_with_empty_moves():
    moves = []
    expected_result = []
    assert run(moves, moves_description) == expected_result


def test_run_with_invalid_moves():
    moves = ["x", "y", "z"]
    expected_result = []
    assert run(moves, moves_description) == expected_result
