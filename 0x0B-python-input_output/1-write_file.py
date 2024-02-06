#!/usr/bin/python3
"""Defining a file-writing func."""


def write_file(filename="", text=""):
    """Write the strng to a UTF8 text file.

    Args:
        filename (str): Name of the file to write.
        text (str): Text to write to the file.
    Returns:
        The num of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
