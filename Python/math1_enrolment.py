# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Math 1 enrolment (https://www.codechef.com/problems/M1ENROL)

"""
For the upcoming semester. the admins of your university decided to keep a total of X seats for the
MATH-I course. A student interest survey was conducted by the admins and it was found that Y
students were interested in taking up the RATH-I course.
Find the minimum number of extra seats that the admins need to add into the MATH-I course to make
sure that every student who is interested in taking the course would be able to do so.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    dif = y - x
    print(dif if dif > 0 else 0)
