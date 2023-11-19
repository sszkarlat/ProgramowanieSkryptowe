import time
from model.core import Vector2d, MoveDirection
from model.animal import Animal
from model.interface import IWorldMap


class OptionsParser:
    @staticmethod
    def parse(args: list[str]) -> list[MoveDirection]:
        mapping = {'f': MoveDirection.FORWARD, 'b': MoveDirection.BACKWARD, 'l': MoveDirection.LEFT, 'r': MoveDirection.RIGHT}
        return list(map(lambda x: mapping[x], filter(lambda x: x in mapping, args)))


class Simulation:
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d], iwmap: IWorldMap) -> None:
        self.directions = directions
        self.positions = positions
        self.animals: list[Animal] = []
        self.iwmap = iwmap

        for vector in self.positions:
            if self.iwmap.place(Animal(vector)):
                self.animals.append(Animal(vector))

    def run(self) -> None:
        for i in range(len(self.directions)):
            print(self.iwmap)
            time.sleep(1)
            
            n = i % len(self.animals)
            self.iwmap.move(self.animals[n],self.directions[i])