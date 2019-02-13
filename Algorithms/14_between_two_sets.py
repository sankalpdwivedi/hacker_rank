#!/bin/python

from __future__ import print_function

import os
import sys

def getTotalX(a, b):
    a = sorted(a)
    b = sorted(b)
    total = 0
    for each in xrange(a[-1], b[0] + 1):
        move_on = False
        for number in a:
            if each % number != 0:
                move_on = True
                break
        if move_on:
            continue
        for number in b:
            if number % each != 0:
                move_on = True
                break
        if move_on:
            continue
        total += 1
    return total


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
