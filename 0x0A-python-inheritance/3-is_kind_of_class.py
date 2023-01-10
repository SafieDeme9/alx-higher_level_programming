#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Test if object is an instance of a class or inherited
    Args:
        @obj (any): The object to check
        @a_class (type): the class
    Returns:
        -True if the object is exactly an instance of
        the specified class ;
        otherwise -False.
    """
    return isinstance(obj, a_class)
