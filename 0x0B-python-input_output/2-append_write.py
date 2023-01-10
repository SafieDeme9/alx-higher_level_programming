#!/usr/bin/python3
"""write_file function"""


def append_write(filename="", text=""):
    """appends a string to the end of a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        number_of_lines = f.write(text)
        return number_of_lines
