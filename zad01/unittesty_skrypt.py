from skrypt import display, run, move_description
import unittest
from unittest.mock import patch
import io


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
