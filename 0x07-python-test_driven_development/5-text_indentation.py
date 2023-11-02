#!/usr/bin/python3

""" Formatting text """


def text_indentation(text):
    """ Printing a string with conditional formatting """
    if not isinstance(text, (str)):
        raise TypeError("text must be a string")

    end_characters = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in end_characters:
            lines.append(current_line.strip())
            lines.append("\n\n")
            current_line = ""

    lines.append(current_line.strip())

    for line in lines:
        print(line, end="")
