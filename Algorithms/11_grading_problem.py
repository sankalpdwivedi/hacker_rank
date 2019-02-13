#!/bin/python


import os
import sys


# Complete the gradingStudents function below.
def gradingStudents(grades):
    for each in grades:
        if each < 38:
            print str(each)
        elif each % 5 < 3:
            print str(each)
        else:
            print (each + (5 - each % 5))


if __name__ == '__main__':

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    gradingStudents(grades)

