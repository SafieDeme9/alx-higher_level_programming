#!/usr/bin/python3
"""Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        x (int): x
        y (int): y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise the class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if not self.__width or not self.__height:
            print("")
        else:
            rect = "\n" * self.y + (" " * self.x +"#" * self.width + "\n") * self.height
            print(rect, end="")

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def __updArgsKwarg(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method for updating the square"""
        args = locals()
        for k in args.keys():
            if args[k] is not None and k != "self" and k == "id":
                self.__dict__[k] = args[k]
            elif args[k] is not None and k != "self":
                self.__dict__["_" + type(self).__name__ + "__" + k] = args[k]

    def update(self, *args, **kwargs):
        """Updates the square"""
        if args:
            self.__updArgsKwarg(*args)
        elif kwargs:
            self.__updArgsKwarg(**kwargs)

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x,
                "y": self.y}
