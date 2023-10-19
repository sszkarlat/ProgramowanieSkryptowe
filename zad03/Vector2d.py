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
        if self.__x <= other_Vector2d.get_x and self.__y <= other_Vector2d.get_y:
            return True

    def follows(self, other_Vector2d):
        if self.__x >= other_Vector2d.get_x and self.__y >= other_Vector2d.get_y:
            return True

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


# vectors = Vector2d(2, 3)
# vectors2 = Vector2d(2, 3)
# print(vectors)
# # print(vectors.__x)
# # print(vectors.__y)
# print(vectors.precedes(vectors2))
# print(vectors.follows(vectors2))
# print(vectors.add(vectors2))
# print(vectors.subtract(vectors2))
# print(vectors.upperRight(vectors2))
# print(vectors.lowerLeft(vectors2))
# print(vectors.opposite())
# print(vectors.__eq__(vectors2))
