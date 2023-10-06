#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    roman_dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}

    total = 0
    prev_value = 0
    i = 0

    for i in range(len(roman_string)):
        current_value = roman_dico[roman_string[i]]
        if current_value <= prev_value:
            total += current_value
        else:
            total += current_value - 2 * prev_value

        prev_value = current_value

    return total
