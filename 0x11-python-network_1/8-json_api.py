#!/usr/bin/python3
"""
Sends a POST request with a letter as a parameter
to http://0.0.0.0:5000/search_user
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request and display the result
    :param letter: The letter to be sent as a parameter
    """
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        search_user(sys.argv[1])
    else:
        search_user("")
