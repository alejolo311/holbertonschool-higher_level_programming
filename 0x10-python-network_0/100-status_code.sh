#!/bin/bash
# request and return the status code
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
