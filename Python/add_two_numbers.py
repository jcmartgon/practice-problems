# Jesus Carlos Martinez Gonzalez
# 02/08/2023
# Add two numbers (https://www.codechef.com/problems/FLOW001)

"""
Your task is very simple: given two integers A and B, write a program to add these two numbers and output the sum.
"""

T = int(input())
for tc in range(T):
    # Read integers a and b.
    (a, b) = map(int, input().split(" "))

    ans = a + b
    print(ans)
