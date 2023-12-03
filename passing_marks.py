# Jesus Carlos Martinez Gonzalez
# 03/12/2023
# Passing marks (https://www.codechef.com/problems/CUTOFF)

"""
In a class of N students, a class test was held. The student scored Ai marks. It is also known that the
scores of all students were distinct.
A student passes the test if their score is strictly greater than the passing mark. Given that exactly X
students pass in the test, find the maximum value of the passing mark of the test.
"""

for _ in range(int(input())):
    total_students, passed_students = map(int, input().split())
    grades = sorted([int(x) for x in input().split()], reverse=True)

    curr = grades[0]
    for i in range(passed_students):
        curr = grades[i]

    print(curr - 1)
