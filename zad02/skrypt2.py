import sys


def user_enter_data():
    inputData = []
    try:
        while True:
            inputData.append(input())
    except EOFError:
        return inputData


inputData = user_enter_data()
operations = sys.argv[2:]
if sys.argv[1] == "cut":
    from cut import cut

    cut(operations, inputData)
elif sys.argv[1] == "cut":
    from grep import grep

    grep(operations, inputData)
else:
    print("Nie ma takiego polecenia!")
