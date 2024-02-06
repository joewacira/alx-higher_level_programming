#!/usr/bin/python3
"""Defining a class-checking function."""


def is_same_class(obj, a_class):
    """Checking if an object is exactly an instance of given class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If object is exactly an instance of a class - True.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
