# Jesus Carlos Martinez Gonzalez
# 07/10/2023
# Greater average (https://www.codechef.com/problems/AVGPROBLEM)

"""
You are given 3 numbers A, B, and C
Determine whether the average of A and B is strictly greater than C or not?
NOTE: Average of A and B is defined as —y— . For example. average of 5 and 9 is 7. average of 5 and
8 is 6.5.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if (a + b) / 2 > c else "NO")
