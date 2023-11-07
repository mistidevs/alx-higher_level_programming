#!/usr/bin/python3
""" Inserts a line of text to a file after each line
with a specific string """


def append_after(filename="", search_string="", new_string=""):
    """ Appending a string to a text chunk """
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = line + new_string

        f.seek(0)
        f.writelines(lines)


if __name__ == '__main__':
    append_after()
