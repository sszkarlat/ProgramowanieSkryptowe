from OptionsParser import OptionsParser


def test_run():
    assert OptionsParser.run(
        ["FORWARD", "BACKWARD", "LEFT", "RIGHT", "LE", "XYX", "RIGHT"]
    ) == ["FORWARD", "BACKWARD", "LEFT", "RIGHT", "RIGHT"]
    assert OptionsParser.run(["LEFT", "LEFT", "LEFT", "XYX", "RIGT", "MIS"]) == [
        "LEFT",
        "LEFT",
        "LEFT",
    ]
    assert OptionsParser.run(["XYZ", "MIS", "LEWO", "PRAWO"]) == []
