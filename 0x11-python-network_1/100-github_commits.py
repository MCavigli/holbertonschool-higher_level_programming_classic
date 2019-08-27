#!/usr/bin/python3
# user Github API to list 10 commits from specific user in specific repo
import requests
import sys


if __name__ == "__main__":
    # user Github API to list 10 commits from specific user in specific repo
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        r = requests.get(url)
        r_json = r.json()
        if len(r_json) > 10:
            length = 10
        for i in range(length):
            print("{}: {}".format(r_json[i].get('sha'),
                                  r_json[i].get('commit')
                                  .get('author').get('name')))
    except:
        print("None")
