from typing_extensions import Self
from enum import Enum, IntEnum


class MoveDirection(Enum):
    FORWARD = 0
    BACKWARD = 1
    LEFT = 2
    RIGHT = 3


class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def get_x(self):
        return self.__x

    @get_x.getter
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    @get_y.getter
    def get_y(self):
        return self.__y

    def precedes(self, other_Vector2d):
        return (
            True
            if self.__x <= other_Vector2d.get_x and self.__y <= other_Vector2d.get_y
            else False
        )

    def follows(self, other_Vector2d):
        return (
            True
            if self.__x >= other_Vector2d.get_x and self.__y >= other_Vector2d.get_y
            else False
        )

    def add(self, other_Vector2d):
        x = self.__x + other_Vector2d.get_x
        y = self.__y + other_Vector2d.get_y
        return Vector2d(x, y)

    def subtract(self, other_Vector2d):
        x = self.__x - other_Vector2d.get_x
        y = self.__y - other_Vector2d.get_y
        return Vector2d(x, y)

    def upperRight(self, other_Vector2d):
        x = self.__x if self.__x >= other_Vector2d.get_x else other_Vector2d.get_x
        y = self.__y if self.__y >= other_Vector2d.get_y else other_Vector2d.get_y
        return Vector2d(x, y)

    def lowerLeft(self, other_Vector2d):
        x = self.__x if self.__x <= other_Vector2d.get_x else other_Vector2d.get_x
        y = self.__y if self.__y <= other_Vector2d.get_y else other_Vector2d.get_y
        return Vector2d(x, y)

    def opposite(self):
        x = self.__x * (-1)
        y = self.__y * (-1)
        return Vector2d(x, y)

    def __eq__(self, other_Vector2d):
        return self.__x == other_Vector2d.get_x and self.__y == other_Vector2d.get_y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class MapDirection(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def next(self) -> "MapDirection":
        nextValue = (self.value + 1) % 4
        return MapDirection(nextValue)

    def previous(self) -> "MapDirection":
        previousValue = (self.value - 1) % 4
        return MapDirection(previousValue)

    def toUnitVector(self) -> "Vector2d":
        orientationToVector = {
            0: Vector2d(0, 1),  # NORTH
            1: Vector2d(1, 0),  # EAST
            2: Vector2d(0, -1),  # SOUTH
            3: Vector2d(-1, 0),  # WEST
        }

        return orientationToVector.get(self.value, Vector2d(0, 0))

    def __str__(self) -> str:
        orientationOfVector = {0: "↑", 1: "→", 2: "↓", 3: "←"}
        return orientationOfVector.get(self.value, "")


class Animal:
    def __init__(self, position: Vector2d, orientation=MapDirection.NORTH) -> None:
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return str(self.position)