
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(n, arr):
    pos = 0
    neg = 0
    zero = 0

    for each in arr:
        if each > 0:
            pos += 1
        elif each < 0:
            neg += 1
        elif each == 0:
            zero += 1
    print float(pos) / n
    print float(neg) / n
    print float(zero) / n


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(n, arr)

