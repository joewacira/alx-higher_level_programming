#!/usr/bin/python3

def safe_print_integer(value):
    """Print an int with "{:d}".format().

    Args:
        value (int): The int to get printed.

    Returns:
        If TypeError/ValueError - (False).
        else - (True).
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
