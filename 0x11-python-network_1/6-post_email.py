#!/usr/bin/python3
"""
Sends a POST request with an email parameter to a given URL
"""

import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with provided email parameter.
    :param url: The URL to send the POST request to.
    :param email: The email to be sent as a parameter.
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    # Checks if both URL and email are provided as command line arguments
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Sends POST request and display response
    send_post_request(url, email)
