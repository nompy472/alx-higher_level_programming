#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me using curl in silent mode
curl -sX PUT 0.0.0.0:5000/catch_me -L -d "user_id=98" -H "Origin: HolbertonSchool"
