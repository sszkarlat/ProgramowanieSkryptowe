from MoveDirection import MoveDirection
from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument("arguments", nargs="*", help="arguments")
args = arg_parser.parse_args().arguments


class OptionsParser:
    @staticmethod
    def run(moves, moveDirection):
        MoveDirection = []
        for move in moves:
            if move in moveDirection:
                MoveDirection.append(move)

        return MoveDirection


option = OptionsParser.run(args, MoveDirection)
print(option)
