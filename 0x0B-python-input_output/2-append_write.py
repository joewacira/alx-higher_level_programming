#!/usr/bin/python3
"""Defining a file-appending function."""


def append_write(filename="", text=""):
    """Appending a strng to the end of a UTF8 text file.

    Args:
        filename (str): Name of the file to append to.
        text (str): String to append to the file.
    Returns:
        The num of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
