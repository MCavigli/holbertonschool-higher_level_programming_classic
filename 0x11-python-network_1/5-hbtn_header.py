#!/usr/bin/python3
# Module that displays value of variable X-Request-Id
import requests
import sys


if __name__ == "__main__":
    # displays value of variable X-Request-Id
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
