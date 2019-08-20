#!/bin/bash
# Sends POST request and displays body response
curl -sX "POST" "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
