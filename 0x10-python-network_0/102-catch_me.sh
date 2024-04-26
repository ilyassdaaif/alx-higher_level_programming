#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!"

# Make a request to the server using curl
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool" -L -o /dev/null -w "You got me!"
