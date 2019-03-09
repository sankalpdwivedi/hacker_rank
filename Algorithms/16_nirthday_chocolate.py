#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    """m numbers in s whose sum is d"""
    result = 0
    for index, each in enumerate(s):
        if index + m > len(s):
            break
        total = 0
        for j in range(0, m):
            total += s[index + j]
        if total == d:
            result += 1 
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    s = map(int, raw_input().rstrip().split())

    dm = raw_input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

