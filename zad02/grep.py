import sys

# options = sys.argv[1:]
# options = ["-i", "bin"]
# inputData = ["/usr/sbin/nologin", "/bin/sync", "/BIN/"]


def sprawdzenie_separator(inputData):
    if "/" in inputData[0]:
        separator = "/"
    elif " " in inputData[0]:
        separator = " "
    elif ":" in inputData[0]:
        separator = ":"

    return separator


def grep(options, inputData):
    outData = []
    separator = sprawdzenie_separator(inputData)
    inputDataSplit = [j.split(separator) for j in inputData]
    for i in range(0, len(options), 2):
        if options[i] == "-i":
            if options[i + 1] == "-w":
                pattern = options[i + 2]
                for j in range(len(inputDataSplit)):
                    for k in inputDataSplit[j]:
                        if k.lower() == pattern.lower():
                            outData.append(inputData[j])
            else:
                pattern = options[i + 1]
                for j in inputData:
                    if pattern.lower() in j.lower():
                        outData.append(j)
        elif options[i] == "-w":
            if options[i + 1] == "-i":
                pattern = options[i + 2]
                for j in range(len(inputDataSplit)):
                    for k in inputDataSplit[j]:
                        if k.lower() == pattern.lower():
                            outData.append(inputData[j])
            else:
                pattern = options[i + 1]
                for j in range(len(inputDataSplit)):
                    for k in inputDataSplit[j]:
                        if k == pattern:
                            outData.append(inputData[j])
        else:
            pattern = options[i]
            for j in inputData:
                if pattern in j:
                    outData.append(j)

    for line in outData:
        print(line)


# grep(options, inputData)
