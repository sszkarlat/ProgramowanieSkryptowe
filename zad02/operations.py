def first_character(string):
    return string[0]


def first_two_characters(string):
    return string[:2] if len(string) > 1 else ""


def all_characters_except_first_two(string):
    return string[2:]


def penultimate_character(string):
    return string[-2] if len(string) > 1 else ""


def last_three_characters(string):
    return string[-3:] if len(string) > 2 else ""


def all_characters_in_even_positions(string):
    return string[::2]


def merge_characters_and_duplicate(string):
    return (first_character(string) + penultimate_character(string)) * len(string)
