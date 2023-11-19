from model.core import MoveDirection, Vector2d
from model.animalOldVersion import Animal


class OptionsParser:
    @staticmethod
    def parse(stringList):
        resultList = []
        for string in stringList:
            if string == "f":
                resultList.append(MoveDirection["FORWARD"])
            elif string == "b":
                resultList.append(MoveDirection["BACKWARD"])
            elif string == "l":
                resultList.append(MoveDirection["LEFT"])
            elif string == "r":
                resultList.append(MoveDirection["RIGHT"])
            else:
                raise ValueError(f'{string} is not legal move specification')

        return resultList


class Simulation:
    def __init__(
        self, directions: list[MoveDirection], positions: list[Vector2d]
    ) -> None:
        self.directions = directions
        self.animals = [Animal(position) for position in positions]

    def run(self) -> None:
        for i, direction in enumerate(self.directions):
            index = i % len(self.animals)
            self.animals[index].move(direction)
            print(f"Zwierzę {index} : {self.animals[index]}")