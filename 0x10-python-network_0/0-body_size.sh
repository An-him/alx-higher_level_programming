#!/bin/bash
# script sends a requests and displays size of body
curl -s -w '%{size_download}\n' -o /dev/null "$1"
