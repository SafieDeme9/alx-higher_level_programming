#!/bin/bash
#sends GET request to the URL and display the body response
curl -sfL "$1" -X GET
