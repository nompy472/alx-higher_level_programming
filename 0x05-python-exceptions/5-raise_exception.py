#!/usr/bin/python3

def raise_exception():

    """Raise a TypeError exception."""

    try:
        raise None
    except Exception:
        raise TypeError
