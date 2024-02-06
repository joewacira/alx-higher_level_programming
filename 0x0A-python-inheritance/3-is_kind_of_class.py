#!/usr/bin/python3
"""Defining a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checking if an object is an instance / inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If object is an instance or inherited instance of a_class - True.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
