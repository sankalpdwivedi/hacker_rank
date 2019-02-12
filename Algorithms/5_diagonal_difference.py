# !/bin/python

import os


# Complete the diagonalDifference function below.
def diagonalDifference(arr, n):
    i = 0
    j = 0
    k = n - 1
    sum_d1 = 0
    sum_d2 = 0
    while i < n:
        sum_d1 += arr[i][j]
        sum_d2 += arr[i][k]
        i += 1
        j += 1
        k -= 1
    return abs(sum_d1 - sum_d2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
