from core import MoveDirection, Vector2d, MapDirection

class Animal:
    def __init__(self, position: Vector2d, orientation = MapDirection.NORTH) -> None:
        self.position = position
        self.orientation = orientation

    def isAt(self, position: Vector2d) -> bool:
        return True if position.__eq__ else False

    def move(self, direction: MoveDirection) -> None:
        if direction.value == MoveDirection.RIGHT.value:
            self.orientation = self.orientation.next()
        
        elif direction.value == MoveDirection.LEFT.value:
            self.orientation = self.orientation.previous()
        
        if direction.value == MoveDirection.FORWARD.value or direction.value == MoveDirection.BACKWARD.value:
            if direction.value == MoveDirection.FORWARD.value:
                target: Vector2d = self.position.add(self.orientation.toUnitVector())
            else:
                target = self.position.subtract(self.orientation.toUnitVector())
            if target.precedes(Vector2d(4,4)) and target.follows(Vector2d(0,0)):
                self.position = target
                
    def __str__(self) -> str:
        return f'{self.position} {self.orientation}'

    def __repr__(self) -> str:
        return str(self)