from controller import OptionsParser


def test_options_parser():
    assert OptionsParser.options_parser(["f", "b", "l", "e", "x", "r"]) == [0, 1, 2, 3]
    assert OptionsParser.options_parser(["l", "l", "l", "x", "ri", "mis"]) == [2, 2, 2]
    assert OptionsParser.options_parser(["x", "mis", "lew", "prawo"]) == []
