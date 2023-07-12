#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from typing import List
from json import dump, load


def save_to_json_file(my_obj: List, filename: str) -> None:
    """Save an object to a JSON file."""
    with open(filename, 'w') as file:
        dump(my_obj, file)


def load_from_json_file(filename: str) -> List:
    """Load an object from a JSON file."""
    with open(filename, 'r') as file:
        return load(file)


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
