# Jesus Carlos Martinez Gonzalez
# 31/08/2023
# Find remainder (https://www.codechef.com/problems/FLOW002)

"""
Write a program to find the remainder when an integer A is divided by an integer B.
"""

# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a % b)
