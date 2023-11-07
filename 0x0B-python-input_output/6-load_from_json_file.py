#!/usr/bin/python3
""" Returning a PyObject from a JSON file """
import json


def load_from_json_file(filename):
    """ Using dumps to return a PyObject from JSON file """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())


if __name__ == '__main__':
    load_from_json_file()
