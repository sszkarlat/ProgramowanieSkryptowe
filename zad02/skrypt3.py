import argparse
from cut import cut
from grep import grep
import operations


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
        "arguments", nargs="*", help="Additional arguments for the 'cut' command"
    )

    # Subparser for "grep" command
    grep_parser = subparsers.add_parser("grep", help="Grep command")
    grep_parser.add_argument(
        "arguments", nargs="*", help="Additional arguments for the 'grep' command"
    )

    # Subparser for "string operations" command
    operations_parser = subparsers.add_parser(
        "string_operations", help="String operations command"
    )
    operations_parser.add_argument("string", help="Input string")

    args = parser.parse_args()

    if args.command == "cut":
        cut(args.arguments, user_enter_data())
    elif args.command == "grep":
        grep(args.arguments, user_enter_data())
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
