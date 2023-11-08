from typing import Self
from enum import Enum, IntEnum


class MoveDirection(Enum):
    FORWARD = 0
    BACKWARD = 1
    LEFT = 2
    RIGHT = 3


print(MoveDirection.LEFT.value)


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

    # Dodaj metodę __eq__ do porównywania dwóch obiektów Vector2d
    def __eq__(self, other):
        if isinstance(other, Vector2d):
            return self.__x == other.get_x and self.__y == other.get_y
        return False

    # Dodaj metodę __hash__ do umożliwienia haszowania obiektów Vector2d
    def __hash__(self):
        return hash((self.__x, self.__y))

    def __str__(self):
        return f"({self.__x},{self.__y})"


class MapDirection(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def next(self) -> "MapDirection":
        nextValue = (self.value + 1) % len(MapDirection)
        return MapDirection(nextValue)

    def previous(self) -> "MapDirection":
        previousValue = (self.value - 1) % len(MapDirection)
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

    def isAt(self, position: Vector2d) -> bool:
        return True if position.__eq__ else False

    def move(self, direction: MoveDirection) -> None:
        # if direction in {MoveDirection.LEFT, MoveDirection.RIGHT}:
        #     if direction == MoveDirection.LEFT:
        #         self.orientation = self.orientation.previous()
        #     else:
        #         self.orientation = self.orientation.next()
        # else:
        #     new_position = self.position.add(self.orientation.toUnitVector())

        #     if 0 <= new_position.get_x < 4 and 0 <= new_position.get_y < 4:
        #         self.position = new_position

        if direction.value == 0:
            if self.orientation.value == 0 and 0 <= self.position.get_y < 4:
                self.position = self.position.add(self.orientation.toUnitVector())
            elif self.orientation.value == 1 and 0 <= self.position.get_x < 4:
                self.position = self.position.add(self.orientation.toUnitVector())
            elif self.orientation.value == 2 and 0 < self.position.get_y <= 4:
                self.position = self.position.add(self.orientation.toUnitVector())
            elif self.orientation.value == 3 and 0 < self.position.get_x <= 4:
                self.position = self.position.add(self.orientation.toUnitVector())
        elif direction.value == 1:
            if self.orientation.value == 0 and 0 < self.position.get_y <= 4:
                self.position = self.position.subtract(self.orientation.toUnitVector())
            elif self.orientation.value == 1 and 0 < self.position.get_x <= 4:
                self.position = self.position.subtract(self.orientation.toUnitVector())
            elif self.orientation.value == 2 and 0 <= self.position.get_y < 4:
                self.position = self.position.subtract(self.orientation.toUnitVector())
            elif self.orientation.value == 3 and 0 <= self.position.get_x < 4:
                self.position = self.position.subtract(self.orientation.toUnitVector())
        elif direction == MoveDirection.LEFT:
            self.orientation = self.orientation.previous()
        elif direction == MoveDirection.RIGHT:
            self.orientation = self.orientation.next()

    def __str__(self) -> str:
        return f"{self.position} {self.orientation}"

    def __repr__(self) -> str:
        return str(self)
