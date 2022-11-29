#!/usr/bin/python3
for letter_code in range(ord('a'), ord('z')+1):
    if letter_code != ord('q') and letter_code != ord('e'):
        print("{:c}".format(letter_code), end='')
