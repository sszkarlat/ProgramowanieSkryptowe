import time
from model.core import Vector2d, MoveDirection
from model.animal import Animal
from model.interface import IWorldMap

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

        return resultList


class Simulation:
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d], iwmap: IWorldMap) -> None:
        self.directions = directions
        self.positions = positions
        self.animals: list[Animal] = []
        self.iwmap = iwmap

        for v in self.positions:
            if self.iwmap.place(Animal(v)):
                self.animals.append(Animal(v))
    
    def run(self) -> None:
        for i in range(len(self.directions)):
            print(self.iwmap)
            time.sleep(1)
        # print(self.directions)
        # print(self.animals)
            n = i % len(self.animals)
            self.iwmap.move(self.animals[n],self.directions[i])
