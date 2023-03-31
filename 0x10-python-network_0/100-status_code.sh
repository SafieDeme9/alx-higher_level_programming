#!/bin/bash
#send request and displays status code
curl -sI "$1" -o /dev/null -w "%{http_code}"
