# Jesus Carlos Martinez Gonzalez
# 11/12/2023
# Group assignment (https://www.codechef.com/problems/GROUPASSGN)

"""
Chef's professor is planning to give his class a group assignment. There are 2N students in the class,
with distinct roll numbers ranging from 1 to 2N. Chefs roll number is X.
The professor decided to create N groups of 2 students each. The groups were created as follows: the
first group consists of roll numbers I and 2N, the second group of roll numbers 2 and 2N — I, and so
on, with the final group consisting of roll numbers N and N + 1.
Chef wonders who his partner will be. Can you help Chef by telling him the roll number of his partner?
"""

for _ in range(int(input())):
    n, chef = map(int, input().split())
    n *= 2

    print(n - chef + 1)
