#!/bin/bash

# Send the POST request and display the response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
