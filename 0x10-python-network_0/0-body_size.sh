#!/bin/bash
# Displays body size of URL
curl -sI "$1" | grep "Content-Length" | cut -d ':' -f 2 | cut -d ' ' -f 2
