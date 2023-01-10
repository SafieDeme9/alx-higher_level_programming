#!/usr/bin/python3
"""is_same_class function"""


def is_same_class(obj, a_class):
    """Test if object is an instance of a classe
    Args:
        @obj (any): The object to check
        @a_class (type): the class
    Returns:
        -True if the object is exactly an instance of
        the specified class ;
        otherwise -False.
    """
    return type(obj) == a_class
