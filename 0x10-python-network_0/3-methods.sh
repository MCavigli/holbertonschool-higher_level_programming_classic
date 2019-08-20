#!/bin/bash
# Displays all acceptable HTTP methods
curl -siX "OPTIONS" "$1" | grep "Allow:" | cut -d ' ' -f 2-
