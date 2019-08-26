#!/usr/bin/python3
# Module with code that sends email POST request
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    # sends email POST request
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as request:
        html = request.read()
    print(html.decode('utf-8'))
