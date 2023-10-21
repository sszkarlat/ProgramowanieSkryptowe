from MoveDirection import MoveDirection
from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument("arguments", nargs="*", help="arguments")
args = arg_parser.parse_args().arguments


class OptionsParser:
    @staticmethod
    def run(stringList):
        s = []
        for move in stringList:
            if move in [item.value for item in MoveDirection]:
                s.append(move)

        return s


print(args)
option = OptionsParser.run(args)
print(option)
