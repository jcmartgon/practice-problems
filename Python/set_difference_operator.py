# Jesus Carlos Martinez Gonzalez
# 11/06/2023
# Set Difference Operation (https://www.hackerrank.com/challenges/py-set-difference-operation/problem)

"""
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
"""

if __name__ == "__main__":
    n = int(input())
    english = set(input().split())
    m = int(input())
    french = set(input().split())
    print(len(english.difference(french)))
