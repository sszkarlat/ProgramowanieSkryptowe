from enum import Enum


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


# position1 = Vector2d(1, 2)
# print(position1)  # (1,2)
# position2 = Vector2d(-2, 1)
# print(position2)  # (-2,1)
# print(position1.add(position2))  # (-1,3)
# print(position1.subtract(position2))  # (3,1)
# print(position1.lowerLeft(position2))  # (-2,1)
# print(position1.upperRight(position2))  # (1,2)
# print(position1.precedes(position2))  # False
# print(position1.follows(position2))  # True
# print(position1.opposite())  # (-1,-2)
# print(position1.__eq__(position2))  # False
