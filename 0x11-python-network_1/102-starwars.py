#!/usr/bin/python3
# searches for Star Wars name with string and lists movies
import requests
import sys


if __name__ == "__main__":
    # seraches for Star Wars name with string and lists movies
    name = sys.argv[1]
    url = 'https://swapi.co/api/people/?search=' + name
    r = requests.get(url)
    json_r = r.json()
    print("Number of results: {}".format(json_r.get('count')))
    for n in json_r.get('results'):
        print(n.get('name'))
        films = n.get('films')
        for t in range(len(films)):
            _title = requests.get(films[t]).json()
            print("\t{}".format(_title.get('title')))
    while json_r.get('next'):
        url = json_r.get('next')
        r = requests.get(url)
        json_r = r.json()
        for n in json_r.get('results'):
            print(n.get('name'))
            films = n.get('films')
            for t in range(len(films)):
                _title = requests.get(films[t]).json()
                print("\t{}".format(_title.get('title')))
