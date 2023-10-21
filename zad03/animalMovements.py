import sys
from OptionsParser import OptionsParser

moveDescription = {
    0: "Zwierzak idzie do przodu",
    1: "Zwierzak idzie do tyłu",
    2: "Zwierzak skręca w lewo",
    3: "Zwierzak skręca w prawo",
}


def display(args, show_index):
    print("Start")
    if show_index:
        for i in range(len(args)):
            print(f"args[{i}] = {args[i]}")
    else:
        for arg in args:
            print(arg)
    print("Stop")


def run(moves, moveDescription):
    result = []
    for i in moves:
        if i in moveDescription.keys():
            result.append(moveDescription[i])

    return result


if __name__ == "__main__":
    options = OptionsParser()
    movesList = options.options_parser(sys.argv)

    display(run(movesList, moveDescription), False)
