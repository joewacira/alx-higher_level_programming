#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If ValueError msg is caught, a similar
    msg is printed to standard error.

    Args:
        value (int): The int to print.

    Returns:
        If TypeError/ValueError occurs - False.
        else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
