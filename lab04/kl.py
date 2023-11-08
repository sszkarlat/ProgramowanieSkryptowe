class Number:
    nextId = 1
    def __init__(self):
        self.id = Number.nextId
        Number.nextId += 1

    def __str__(self):
        return str(self.id)

numberList = [Number() for _ in range(10)]
for number in numberList:
    print(number)