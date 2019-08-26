#!/usr/bin/python3
# Module with code that fetches a URL and displays X-Request-Id variable
import urllib.request
import sys


if __name__ == "__main__":
    # fetches a URL and displays X-Request-Id variable
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
    print(header)
