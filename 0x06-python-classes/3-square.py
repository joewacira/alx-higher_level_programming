#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("the size must be an int")
        elif size < 0:
            raise ValueError("the size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of square."""
        return (self.__size * self.__size)
