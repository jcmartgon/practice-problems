# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# AB difference (https://www.codechef.com/problems/ABDIFF)

"""
Chef is taking his baby steps into the world of programming.
The very first program he's tasked to write is as follows:
"Given two integers A and B, print A + B."
Unfortunately, Chef makes a typo: his program outputs A X B instead of A + B.
Given the values of A and B, can you help Chef find the absolute difference between the correct
answer and the value his program prints?
"""

x, y = map(int, input().split())
print(abs(x * y - (x + y)))
