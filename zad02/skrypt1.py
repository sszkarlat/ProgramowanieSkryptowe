import operations
import sys

string = sys.argv[1]
print(
    f"""{operations.first_character(string)}
{operations.first_two_characters(string)}
{operations.all_characters_except_first_two(string)}
{operations.penultimate_character(string)}
{operations.last_three_characters(string)}
{operations.all_characters_in_even_positions(string)}
{operations.merge_characters_and_duplicate(string)}"""
)
