
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    candles = 0
    ar = sorted(ar, reverse=True)
    for each in ar:
        if each == ar[0]:
            candles += 1
    return candles


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

