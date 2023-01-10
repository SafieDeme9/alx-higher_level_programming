#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters written"""
    with open(filename,mode='w', encoding="utf-8") as f:
        number_of_lines= f.write(text)
        return number_of_lines
