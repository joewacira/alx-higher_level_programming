#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """func print the 1st x elems of a list that are ints.

    Args:
        my_list (list): list to print elems from.
        x (int): The num of elems of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
