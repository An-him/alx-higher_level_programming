#!/bin/bash

# Send the POST request and display the response body
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
