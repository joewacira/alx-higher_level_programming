#!/usr/bin/python3
"""Defining an object attribute lookup function."""


def lookup(obj):
    """Return list of the object's available attributes."""
    return (dir(obj))
