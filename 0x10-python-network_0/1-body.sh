#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the response
curl -s -w "%{http_code}" -o temp_response_body "$1" | grep -q "200$" && cat temp_response_body && rm -f temp_response_body
