import sys

# options = sys.argv[1:]
# options = ["-d", ":", "-f", "1"]


def cut(options, inputData):
    for i in range(0, len(options), 2):
        if options[i] == "-d":
            separator = options[i + 1]
        elif options[i] == "-f":
            columnNumber = int(options[i + 1]) - 1
        else:
            print("Polecenie cut nie ma takiej opcji!")

    for i in inputData:
        print(i.split(separator)[columnNumber])


# zamiast: - musi być znak separator
# zamiast: [0] - musi być kolumna ktora dal user

# inputData = ["ol:pol:gol", "fis:cis:mis", "jop:pop:do", "dd:ss:zz"]
# cut(options, inputData)
