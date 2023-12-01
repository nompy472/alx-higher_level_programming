#!/usr/bin/python3
"""
Send a request to a given URL and display the value of the X-Request-Id header.
"""

import requests
import sys


def get_request_id(url):
    """
    Sends a request to the specified URL
    display the X-Request-Id header value.
    Args:
        url (str): The URL to send the request to.
    Returns:
        None
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    if request_id:
        print(f"X-Request-Id: {request_id}")
    else:
        print("X-Request-Id not found in the response headers.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_request_id(url)
