#!/usr/bin/python3
"""definition of text_indentation function"""


def text_indentation(text):
    """ function text_indentation
    text must be a string
    no space at the beginnig and at the end of the text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    trigger_characters = {'.', '?', ':'}

    for char in text:
        print(char, end='')
        if char in trigger_characters:
            print('\n\n', end='')
