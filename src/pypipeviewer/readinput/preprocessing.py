#!/usr/bin/env python

def catch_exit_condition(answer: str) -> bool:
    if answer == ":q" or answer == ";q" or answer == "=q":
        return True
    return False