#!/bin/bash
# script takes in a URL, displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f2-
