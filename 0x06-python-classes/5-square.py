#!/usr/bin/python3
"""Create a class Square."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)
    
    def my_print(self):
        """Prints the square."""
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
