# Jesus Carlos Martinez Gonzalez
# 09/08/2023
# Second max of three numbers (https://www.codechef.com/problems/SNDMAX)

"""
Write a program that accepts sets of three numbers. and prints the second-maximum numberamong
the three.
"""

for _ in range(int(input())):
    print(sorted(list(map(int, input().split())))[-2])
