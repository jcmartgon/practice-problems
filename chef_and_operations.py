# Jesus Carlos Martinez Gonzalez
# 15/11/2023
# Chef and operations (https://www.codechef.com/problems/CHOPRT)

"""
Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational
Operators.
Relational Operators are operators which check relationship between two values. Given two numerical
values A and B you need to help chef in finding the relationship between them that is,
First one is greater than second or, First one is less than second or, First and second one are equal.
"""


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(">" if a > b else "<" if a < b else "=")
