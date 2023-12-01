#!/bin/bash
# Sends a GET request to the specified URL and displays the body of the response for a 200 status code.
curl -s "$1" -o /dev/null -w "%{http_code}\n" | [ "$(cat)" == "200" ] && curl -s "$1"
