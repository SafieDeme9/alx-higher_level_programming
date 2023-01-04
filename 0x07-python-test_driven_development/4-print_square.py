#!/usr/bin/python3
"""Print a square"""


def print_square(size):
    """Prints square
    Arguments:
        @size: size of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
