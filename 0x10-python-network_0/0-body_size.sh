#!/bin/bash
# Sends a request to the specified URL using curl in silent mode.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' 
