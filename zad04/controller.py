from model import MoveDirection, Vector2d, Animal


class OptionsParser:
    @staticmethod
    def options_parser(stringList):
        resultList = []
        for string in stringList:
            if string == "f":
                resultList.append(MoveDirection["FORWARD"].value)
            elif string == "b":
                resultList.append(MoveDirection["BACKWARD"].value)
            elif string == "l":
                resultList.append(MoveDirection["LEFT"].value)
            elif string == "r":
                resultList.append(MoveDirection["RIGHT"].value)

        return resultList


class Simulation:
    def __init__(
        self, directions: list[MoveDirection], positions: list[Vector2d]
    ) -> None:
        self.directions = directions
        self.animals = [Animal(position) for position in positions]
        # self.lenPositions

    def run(self) -> None:
        for i in range(0, len(self.directions), len(self.animals)):


    def __str__(self):
        for i in self.animals:
            print(i)
