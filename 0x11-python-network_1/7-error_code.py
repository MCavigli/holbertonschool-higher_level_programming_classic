#!/usr/bin/python3
# Module that handles error codes
import requests
import sys


if __name__ == "__main__":
    # handles error codes
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
