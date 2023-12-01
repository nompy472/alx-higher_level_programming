#!/bin/bash
# Sends a POST request to a specified URL with email and subject variables
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
