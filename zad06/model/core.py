#!/usr/bin/python

from typing import Self
from enum import IntEnum

class MoveDirection(IntEnum):
    FORWARD = 0
    BACKWARD = 1
    LEFT = 2
    RIGHT = 3


def log(func):
    def wrapper(*args, **kwargs):
        print(f'Nazwa kwalifikowana: {func.__qualname__}')
        args_str = ' '.join(map(str, args))
        print(f'Argumenty: {args_str}')
        return func(*args, **kwargs)
    return wrapper

def log_to(file):
    def log(func):
        def wrapper(*args, **kwargs):
            args_str = ' '.join(map(str, args))
            with open(file, 'a') as f:
                f.writelines(f'{func.__qualname__}\t| {args_str}\n')
            return func(*args, **kwargs)
        return wrapper
    return log


class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    @log_to('dziennik')
    def get_x(self):
        return self.__x

    @property
    @log
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

    @log_to(file='dziennik')
    def add(self, other_Vector2d):
        x = self.__x + other_Vector2d.get_x
        y = self.__y + other_Vector2d.get_y
        return Vector2d(x, y)

    @log
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
