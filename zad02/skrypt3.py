import argparse
from grep import word_between_separator
import operations


def cut(delimiter, field, inputData):
    for i in inputData:
        print(i.split(delimiter)[field])


def grep(ignore_case, whole_word, pattern, inputData):
    outData = []
    if whole_word:
        if ignore_case:
            for line in inputData:
                if word_between_separator(pattern.lower(), line.lower()):
                    outData.append(line)
        else:
            for line in inputData:
                if word_between_separator(pattern, line):
                    outData.append(line)

    else:
        if ignore_case:
            for line in inputData:
                if pattern.lower() in line.lower():
                    outData.append(line)
        else:
            for line in inputData:
                if pattern in line:
                    outData.append(line)

    for line in outData:
        print(line)


def user_enter_data():
    inputData = []
    try:
        while True:
            inputData.append(input())
    except EOFError:
        return inputData


def main():
    parser = argparse.ArgumentParser(
        description="Process input data using cut, grep, or perform string operations."
    )
    subparsers = parser.add_subparsers(dest="command", help="Choose a command")

    # Subparser for "cut" command
    cut_parser = subparsers.add_parser("cut", help="Cut command")
    cut_parser.add_argument(
        "-d", dest="delimiter", help="Delimiter for the 'cut' command"
    )
    cut_parser.add_argument("-f", dest="field", help="Field for the 'cut' command")

    # Subparser for "grep" command
    grep_parser = subparsers.add_parser("grep", help="Grep command")
    grep_parser.add_argument(
        "-i", action="store_true", help="Perform a case-insensitive search"
    )
    grep_parser.add_argument("-w", action="store_true", help="Match whole words")
    grep_parser.add_argument("pattern", help="Search pattern")

    # Subparser for "string operations" command
    operations_parser = subparsers.add_parser(
        "string_operations", help="String operations command"
    )
    operations_parser.add_argument("string", help="Input string")

    args = parser.parse_args()

    if args.command == "cut":
        delimiter = args.delimiter
        field = args.field
        cut(delimiter, int(field) - 1, user_enter_data())
    elif args.command == "grep":
        ignore_case = args.i
        print(ignore_case)
        whole_word = args.w
        print(whole_word)
        pattern = args.pattern
        grep(ignore_case, whole_word, pattern, user_enter_data())
    elif args.command == "string_operations":
        string = args.string
        print(
            f"""{operations.first_character(string)}
{operations.first_two_characters(string)}
{operations.all_characters_except_first_two(string)}
{operations.penultimate_character(string)}
{operations.last_three_characters(string)}
{operations.all_characters_in_even_positions(string)}
{operations.merge_characters_and_duplicate(string)}"""
        )
    else:
        print("Nie ma takiego polecenia!")


if __name__ == "__main__":
    main()
