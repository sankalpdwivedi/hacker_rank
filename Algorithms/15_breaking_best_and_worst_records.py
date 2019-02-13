#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best_record = 0
    best_score = scores[0]
    worst_record = 0
    worst_score = scores[0]
    
    for each in scores:
        if each > best_score:
            best_score = each
            best_record += 1
        elif each < worst_score:
            worst_score = each
            worst_record += 1
    return [best_record, worst_record]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
