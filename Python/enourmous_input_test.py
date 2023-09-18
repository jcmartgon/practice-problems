# Jesus Carlos Martinez Gonzalez
# 17/09/2023
# Enormous Input Test (https://www.codechef.com/problems/INTEST)

"""
You are given N integers. Find the count of numbers divisible by K.
"""

# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

(n, k) = map(int, input().split())

ans = 0

for i in range(n):
    x = int(input())
    if x % k == 0:
        ans += 1

print(ans)
