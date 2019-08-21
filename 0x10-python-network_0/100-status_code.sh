#!/bin/bash
# display status code of URL request
curl -s -o /dev/null -w "%{http_code}" "$1"
