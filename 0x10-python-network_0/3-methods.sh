#!/bin/bash
# show the available methods 
curl -sI -X OPTIONS "$1" | grep Allow | cut -d' ' -f1 --complement
