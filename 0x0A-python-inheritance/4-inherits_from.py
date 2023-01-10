#!/usr/bin/python3
"""is_kind_of_class function"""


def inherits_from(obj, a_class):
    """Test if object inherited from class
    Args:
        @obj (any): The object to check
        @a_class (type): the class
    Returns:
        -True if the object inherited  of
        the specified class ;
        otherwise -False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
