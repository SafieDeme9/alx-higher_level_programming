#!/bin/bash
#send request and displays status code
curl -sI "$1" | grep HTTP | cut -d " " -f2
