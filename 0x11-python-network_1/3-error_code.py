#!/usr/bin/python3
# Module with code that mangages error code
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    # displays body of response and manages error code
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as request:
            page = request.read()
        print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
