# Jesus Carlos Martinez Gonzalez
# 04/06/2023
# collections.namedtuple (https://www.hackerrank.com/challenges/py-collections-namedtuple/problem)

"""
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and names.

Your task is to help Dr. Wesley calculate the average marks of the students.
"""

from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())

print(sum([float(Student(*input().split()).MARKS) for _ in range(n)])/n)