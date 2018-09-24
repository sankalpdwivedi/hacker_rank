# Sample Problem

# HackerLand University has the following grading policy:
# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
# If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# For example, grade = 84 will be rounded to 85 but grade = 29 will not be rounded because the rounding would result in a number that is less than 38.
# Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.
# Function Description
# Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.
# gradingStudents has the following parameter(s):
# grades: an array of integers representing grades before rounding
# Input Format
# The first line contains a single integer, n, the number of students.
# Each line i of the n subsequent lines contains a single integer, grades[i], denoting student i's grade.
# Constraints
# 1 <= n <= 60
# 0 <= grades[i] <= 100
# Output Format
# For each grades[i], print the rounded grade on a new line.
# Sample Input 0
# 4
# 73
# 67
# 38
# 33
# Sample Output 0
# 75
# 67
# 40
# 33

# Sample Response
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

