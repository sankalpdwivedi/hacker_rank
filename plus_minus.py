# Problem Statement:

# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
# For example, given the array [1,1,0,-1,-1] there are 5 elements, two positive, two negative and one zero. Their ratios would be 2/5, 2/5 and 1/5. It should be printed as
# 0.400000
# 0.400000
# 0.200000
# Function Description
# Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.
# plusMinus has the following parameter(s):
# arr: an array of integers
# Input Format
# The first line contains an integer, n, denoting the size of the array.
# The second line contains  space-separated integers describing an array of numbers
# arr(arr[0], arr[1], arr[2],..., arr[n-1]).
# Constraints
# 0 < n <= 100
# -100 <= arr[i] <= 100
#
# Output Format
# You must print the following 3 lines:
# A decimal representing of the fraction of positive numbers in the array compared to its size.
# A decimal representing of the fraction of negative numbers in the array compared to its size.
# A decimal representing of the fraction of zeros in the array compared to its size.
# Sample Input
# 6
# -4 3 -9 0 4 1
# Sample Output
# 0.500000
# 0.333333
# 0.166667


# Solution:

# !/bin/python

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for each in arr:
        if each > 0:
            positive += 1
        elif each < 0:
            negative += 1
        else:
            zero += 1
    print "{0:6f}".format(float(positive) / len(arr))
    print "{0:6f}".format(float(negative) / len(arr))
    print "{0:6f}".format(float(zero) / len(arr))


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
