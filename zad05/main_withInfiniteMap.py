import sys
from model.core import Vector2d, MoveDirection
from controller import Simulation, OptionsParser
from model.map import InfiniteMap  

directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:])
positions: list[Vector2d] = [
    Vector2d(2, 2), 
    Vector2d(3, 4),
    Vector2d(4, 8),
    Vector2d(7, 5),
    Vector2d(2, 3),
    Vector2d(3, 2), 
    Vector2d(5, 5),
    Vector2d(10, 10),
    Vector2d(17, 15),
    ]
# Poprzednio
# simulation: Simulation = Simulation(directions, positions)
# Obecnie
simulation: Simulation = Simulation(directions, positions, InfiniteMap())
simulation.run()