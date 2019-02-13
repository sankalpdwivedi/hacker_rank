#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    in_house_apples = 0
    in_house_oranges = 0

    for each in apples:
        if t >= a + each >= s:
            in_house_apples += 1
    for each in oranges:
        if t >= b + each >= s:
            in_house_oranges += 1
    print in_house_apples
    print in_house_oranges


if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)

