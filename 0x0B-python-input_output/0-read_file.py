#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):

    """Print the contents of a UTF8 text file to the stdout."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
