#!/usr/bin/env python

import string
from random import *

def basecode():
    return string.ascii_uppercase + string.digits

def codes(basecodes):
    while True:
        yield "".join(choice(basecodes) for x in range(20))


def main():
    sets = set()
    for code in codes(basecode()):
        if len(sets) < 200:
            sets.add(code)
        else:
            break

    for s in sets:
        print s



if __name__ == "__main__":
    main()