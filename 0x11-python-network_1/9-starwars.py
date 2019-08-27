#!/usr/bin/python3
# searches for Star Wars name with string
import requests
import sys


if __name__ == "__main__":
    # seraches for Star Wars name with string
    name = sys.argv[1]
    url = 'https://swapi.co/api/people/?search=' + name
    r = requests.get(url)
    json_r = r.json()
    print("Number of results: {}".format(json_r.get('count')))
    for n in json_r.get('results'):
        print(n.get('name'))
