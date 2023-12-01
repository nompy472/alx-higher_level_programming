#!/usr/bin/python3
"""
Sends a POST request to the specified URL with an email parameter,
using urllib and sys packages.
Displays the body of the response
decoded in utf-8.
"""

import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the given URL with the provided email parameter.
    :param url: The URL to send the POST request to.
    :param email: The email parameter to include in the request.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
