#!/usr/bin/python3
# uses Github credentials to display ID
import sys
import requests


if __name__ == "__main__":
    # uses Github credentials to display ID
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        url = 'https://api.github.com/user'
        r = requests.get(url, auth=(username, password))
        json_r = r.json()
        print(json_r.get('id'))
    except:
        print("None")
