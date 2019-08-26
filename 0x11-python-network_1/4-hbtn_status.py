#!/usr/bin/python3
# Module that fetches a website
import requests


if __name__ == "__main__":
    # fetches a specific website
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
