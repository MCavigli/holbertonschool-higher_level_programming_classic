#!/usr/bin/python3
# uses Github credentials to display ID
import sys
import requests


if __name__ == "__main__":
    # uses Github credentials to display ID
    username = sys.argv[1]
    password = sys.argv[2]
    url1 = 'https://api.github.com/users/whatever?'
    url2 = 'client_id={}&client_secret={}'.format(username, password)
    url = url1 + url2
    r = requests.get(url)
    json_r = r.json()
    print(json_r.get('id'))
