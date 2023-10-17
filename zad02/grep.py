import sys
import re

# options = sys.argv[1:]
# options = ["-w", "-i", "cis"]
# inputData = ["/cis/fis/nologin", "/mis/cisowianka", "/BIN/"]


def word_between_separator(pattern, text):
    patternRegex = re.compile(r"\b" + pattern + r"\b")
    return bool(patternRegex.search(text))


def grep(options, inputData):
    outData = []
    for i in range(0, len(options), 2):
        if options[i] == "-w":
            if options[i + 1] == "-i":
                pattern = options[i + 2]
                for line in inputData:
                    if word_between_separator(pattern.lower(), line.lower()):
                        outData.append(line)
                break
            else:
                pattern = options[i + 1]
                for line in inputData:
                    if word_between_separator(pattern, line):
                        outData.append(line)
        elif options[i] == "-i":
            if options[i + 1] == "-w":
                pattern = options[i + 2]
                for line in inputData:
                    if word_between_separator(pattern.lower(), line.lower()):
                        outData.append(line)
                break
            else:
                pattern = options[i + 1]
                for line in inputData:
                    if pattern.lower() in line.lower():
                        outData.append(line)
        else:
            pattern = options[i]
            for line in inputData:
                if pattern in line:
                    outData.append(line)

    for line in outData:
        print(line)


# grep(options, inputData)
