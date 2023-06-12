# Jesus Carlos Martinez Gonzalez
# 11/06/2023
# Power - Mod Power (https://www.hackerrank.com/challenges/python-power-mod-power/problem)

"""
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
"""

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())

    print(pow(a, b))
    print(pow(a, b, m))
