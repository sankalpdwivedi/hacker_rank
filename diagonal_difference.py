# Problem Statement:

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal sum = 15. The right to left diagonal sum = 17. Their absolute difference is 2.
# Function description
# Complete the diagonalDifference function in the editor below. It must return an integer representing the absolute diagonal difference.
# diagonalDifference takes the following parameter:
# arr: an array of integers.
# Input Format
# The first line contains a single integer, n, the number of rows and columns in the matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers a[i][j].
# Constraints
# -100 <= arr[i][j] <= 100
# Output Format
# Print the absolute difference between the sums of the matrix's two diagonals as a single integer.
# Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output
# 15


# Solution

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
