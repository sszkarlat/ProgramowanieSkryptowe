import unittest
from unittest.mock import patch
import sys
import pytest
import io


def display(args, show_index):
    print("Start")
    if show_index is True:
        for i in range(len(args)):
            print(f"args[{i}] = {args[i]}")
    else:
        for arg in args:
            print(arg)
    print("Stop")


def run(moves, move_description):
    result = []
    for i in moves:
        if i in move_description.keys():
            result.append(move_description[i])

    return result


move_description = {
    "f": "Zwierzak idzie do przodu",
    "b": "Zwierzak idzie do tyłu",
    "l": "Zwierzak skręca w lewo",
    "r": "Zwierzak skręca w prawo",
}


# display(sys.argv, False)
# args = run(sys.argv[1:], move_description)
# display(args, False)


# Testy pytest dla funkcji display
def test_display_without_index(capsys):
    args = ["1", "2", "3"]
    display(args, False)
    out, err = capsys.readouterr()
    assert out == "Start\n1\n2\n3\nStop\n"


def test_display_with_index(capsys):
    args = ["arg1", "arg2", "arg3"]
    display(args, True)
    out, err = capsys.readouterr()
    assert out == "Start\nargs[0] = arg1\nargs[1] = arg2\nargs[2] = arg3\nStop\n"


# Testy pytest dla funkcji run
def test_run():
    moves = ["f", "b", "l", "r", "x"]
    expected_result = [
        "Zwierzak idzie do przodu",
        "Zwierzak idzie do tyłu",
        "Zwierzak skręca w lewo",
        "Zwierzak skręca w prawo",
    ]
    assert run(moves, move_description) == expected_result


def test_run_with_empty_moves():
    moves = []
    expected_result = []
    assert run(moves, move_description) == expected_result


def test_run_with_invalid_moves():
    moves = ["x", "y", "z"]
    expected_result = []
    assert run(moves, move_description) == expected_result


class TestDisplayFunction(unittest.TestCase):
    def test_display_without_index(self):
        args = ["arg1", "arg2", "arg3"]
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            display(args, False)
            output = mock_stdout.getvalue()
        expected_output = "Start\narg1\narg2\narg3\nStop\n"
        self.assertEqual(output, expected_output)

    def test_display_with_index(self):
        args = ["arg1", "arg2", "arg3"]
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            display(args, True)
            output = mock_stdout.getvalue()
        expected_output = (
            "Start\nargs[0] = arg1\nargs[1] = arg2\nargs[2] = arg3\nStop\n"
        )
        self.assertEqual(output, expected_output)


class TestRunFunction(unittest.TestCase):
    def test_run(self):
        moves = ["f", "b", "l", "r", "x"]
        expected_result = [
            "Zwierzak idzie do przodu",
            "Zwierzak idzie do tyłu",
            "Zwierzak skręca w lewo",
            "Zwierzak skręca w prawo",
        ]
        self.assertEqual(run(moves, move_description), expected_result)

    def test_run_with_empty_moves(self):
        moves = []
        expected_result = []
        self.assertEqual(run(moves, move_description), expected_result)

    def test_run_with_invalid_moves(self):
        moves = ["x", "y", "z"]
        expected_result = []
        self.assertEqual(run(moves, move_description), expected_result)


if __name__ == "__main__":
    unittest.main()
