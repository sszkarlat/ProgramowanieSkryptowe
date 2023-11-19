from core import MoveDirection, Vector2d, MapDirection
from interface import IMoveValidator

class Animal:
    def __init__(self, position: Vector2d, orientation = MapDirection.NORTH) -> None:
        self.position = position
        self.orientation = orientation

    def isAt(self, position: Vector2d) -> bool:
        return True if position.__eq__ else False

    def move(self, direction: MoveDirection, validator: IMoveValidator) -> None:
        direction_actions = {
                MoveDirection.RIGHT.name: lambda: self.orientation.next(),
                MoveDirection.LEFT.name: lambda: self.orientation.previous(),
                MoveDirection.FORWARD.name: lambda: self.position.add(self.orientation.toUnitVector()),
                MoveDirection.BACKWARD.name: lambda: self.position.subtract(self.orientation.toUnitVector())
        }
        action = direction_actions.get(direction.name)

        if action:
            target = action()
            if direction.name in [MoveDirection.BACKWARD.name, MoveDirection.FORWARD.name]:
                if validator.canMoveTo(target):
                    self.position = target
            else:
                self.orientation = target

    def __str__(self) -> str:
        return f'{self.orientation}'

    def __repr__(self) -> str:
        return str(self)
