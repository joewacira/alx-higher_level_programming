#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size):
        """Initializing a new square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("the size must be an integer")
        elif value < 0:
            raise ValueError("the size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with # charact."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
