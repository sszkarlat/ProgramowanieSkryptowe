import sys
from model.core import Vector2d, MoveDirection
from controllerOldVersion import Simulation, OptionsParser

directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:])
positions: list[Vector2d] = [Vector2d(2, 2), Vector2d(3, 4)]
simulation: Simulation = Simulation(directions, positions)
simulation.run()