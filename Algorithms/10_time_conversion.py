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
~
