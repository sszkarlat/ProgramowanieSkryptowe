from Vector2d import Vector2d  # Zaimportuj klasę Vector2d z twojego modułu


def test_get_x():
    vector = Vector2d(1, 2)
    assert vector.get_x == 1


def test_get_y():
    vector = Vector2d(1, 2)
    assert vector.get_y == 2


def test_precedes():
    vector1 = Vector2d(1, 2)
    vector2 = Vector2d(3, 4)
    assert vector1.precedes(vector2) is True
    assert vector2.precedes(vector1) is None


def test_follows():
    vector1 = Vector2d(1, 2)
    vector2 = Vector2d(3, 4)
    assert vector1.follows(vector2) is None
    assert vector2.follows(vector1) is True


def test_add():
    vector1 = Vector2d(1, 2)
    vector2 = Vector2d(3, 4)
    result = vector1.add(vector2)
    assert result.get_x == 4
    assert result.get_y == 6


def test_subtract():
    vector1 = Vector2d(1, 2)
    vector2 = Vector2d(3, 4)
    result = vector1.subtract(vector2)
    assert result.get_x == -2
    assert result.get_y == -2


def test_upperRight():
    vector1 = Vector2d(1, 2)
    vector2 = Vector2d(3, 4)
    result = vector1.upperRight(vector2)
    assert result.get_x == 3
    assert result.get_y == 4


def test_lowerLeft():
    vector1 = Vector2d(1, 2)
    vector2 = Vector2d(3, 4)
    result = vector1.lowerLeft(vector2)
    assert result.get_x == 1
    assert result.get_y == 2


def test_opposite():
    vector = Vector2d(1, 2)
    result = vector.opposite()
    assert result.get_x == -1
    assert result.get_y == -2


def test_eq():
    vector1 = Vector2d(1, 2)
    vector2 = Vector2d(1, 2)
    assert vector1 == vector2


def test_str():
    vector = Vector2d(1, 2)
    assert str(vector) == "(1, 2)"
