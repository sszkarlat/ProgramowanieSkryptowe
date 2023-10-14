import cut


def user_enter_data():
    inputData = []
    try:
        while True:
            inputData.append(input())
    except EOFError:
        return inputData


inputData = user_enter_data()
cut(["-d", ":", "-f", "1"])
