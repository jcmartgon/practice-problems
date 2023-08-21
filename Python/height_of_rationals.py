# Jesus Carlos Martinez Gonzalez
# 20/08/2023
# Height of rationals (https://www.codechef.com/problems/HEIGHTRATION)

"""
In a recent breakthrough in mathematics, the proof utilized a concept called Height.
Consider a fraction a. Its Height is defined as the maximum of its numerator and denominator. So, for
27
example, the Height of would be 19, and the Height of would be 27.
Given a and b, find the Height of a
"""

print(max(list(map(int, input().split()))))
