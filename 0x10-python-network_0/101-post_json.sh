#!/bin/bash
#sends a JSON POST request and displays the body reponse
curl -sL -X POST -d @"$2" -H "Content-Type: application/json" "$1"
