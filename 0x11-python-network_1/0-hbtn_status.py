#!/usr/bin/python3
# Module with code that fetches a URL
import urllib.request


if __name__ == "__main__":
    # fetches a URL
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode("utf-8")))
