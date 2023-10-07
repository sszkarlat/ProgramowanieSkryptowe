import sys


def display(args, show_index):
    print("Start")
    if show_index is True:
        for i in range(len(args)):
            print(f"args[{i}] = {args[i]}")
    else:
        for arg in args:
            print(arg)
    print("Stop")


def run(moves, move_description):
    result = []
    for i in moves:
        if i in move_description.keys():
            result.append(move_description[i])

    return result


move_description = {
    "f": "Zwierzak idzie do przodu",
    "b": "Zwierzak idzie do tyłu",
    "l": "Zwierzak skręca w lewo",
    "r": "Zwierzak skręca w prawo",
}


# display(sys.argv, False)
# args = run(sys.argv[1:], move_description)
# display(args, False)
