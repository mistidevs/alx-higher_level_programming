#!/usr/bin/python3
""" Saving to a JSON file with utf-8 """
import json


def save_to_json_file(my_obj, filename):
    """ Using JSON methods and with """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))


if __name__ == '__main__':
    save_to_json_file()
