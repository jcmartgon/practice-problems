# Jesus Carlos Martinez Gonzalez
# 30/01/2024
# Sums in a triangle (https://www.codechef.com/problems/SUMTRIAN)

"""
Given an integer N, let us consider a triangle of numbers of N lines in which a number all appears in
the first line, two numbers am and an appear in the second line, three numbers au and
appear in the third line, etc. In general, inumbers atl, ao ... aii appear in thet line for all I i < N
. Develop a program that will compute the largest of the sums of numbers that appear on the paths
starting from the top towards the base, so that:
• on each path the next number is located on the row below, more precisely either directly below or
below and one place to the right.
"""

for _ in range(int(input())):
    height = int(input())
    values = []

    # Add triangle values to values list
    for row in range(height):
        values.append([int(x) for x in input().split()])

    # Starting from the second-to-last row, add the larger eligible value from the next row
    for i in range(height - 2, -1, -1):
        for j in range(0, i + 1):
            values[i][j] += max(values[i + 1][j], values[i + 1][j + 1])
    print(values[0][0])
