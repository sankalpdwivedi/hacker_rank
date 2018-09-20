# Problem Statement

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
# Function Description
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
# timeConversion has the following parameter(s):
# s: a string representing time in 12 hour format
# Input Format
# A single string s containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12 and 00 <= mm,ss <= 59.
# Constraints
# All input times are valid
# Output Format
# Convert and print the given time in 24-hour format, where 00 <= hh <= 23.
# Sample Input 0
# 07:05:45PM
# Sample Output 0
# 19:05:45

# Solution
#!/bin/python

import os


# Complete the timeConversion function below.
def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return "00{}".format(s[s[2:-2]])
        return s[:-2]
    return "{}{}".format(int(s[:2]) + 12, s[2:-2])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
