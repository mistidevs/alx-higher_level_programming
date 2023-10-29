#!/usr/bin/python3

""" Addition module
Returns the sum of two numbers
Raises a TypeError if a or b is not an integer
Converts floats to integers first
b is predertimined of not passed """

def add_integer(a, b=98):
    """ Computes the sum of two numbers
    a and b should be floats or integers
    Returns the sum """
    
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")

    if type(a) is bool:
        raise TypeError("a must be an integer")
    if type(b) is bool:
        raise TypeError("b must be an integer")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    add_integer()

    
