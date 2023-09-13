#!/usr/bin/env python

# To add <package> to PYTHONPATH
# https://stackoverflow.com/a/34938623
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../src")

import sys
from pypipeviewer.readinput import preprocessing

def main() -> None:
    prompt = "=>> Search for YouTube videos (:h for help)\n> "
    while True:
        answer = input(prompt)
        exit_condition = preprocessing.catch_exit_condition(answer)
        if exit_condition:
            sys.exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        """ Exit gracefuly with ^C"""
        print()
        sys.exit()
    except EOFError:
        """ Exit gracefuly with ^D"""
        print()
        sys.exit()