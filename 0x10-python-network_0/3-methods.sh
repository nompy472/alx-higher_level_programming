#!/bin/bash
# Retrieves and displays all HTTP methods supported by a server for a given URL
curl -sI "$1" | grep Allow | cut -d' ' -f2-
