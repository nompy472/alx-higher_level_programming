#!/bin/bash
# Sends a JSON POST request to the specified URL with the contents of a file in the request body.
curl -s -X POST -H "Content-Type: application/json" --data "@$2" "$1"
