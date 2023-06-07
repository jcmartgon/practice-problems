# Jesus Carlos Martinez Gonzalez
# 05/06/2023
# collections.namedtuple (https://www.hackerrank.com/challenges/py-collections-namedtuple/problem)

"""
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and names.

Your task is to help Dr. Wesley calculate the average marks of the students.

Challenge: Complete the problem within 4 LOC
"""

from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())

print(sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n)