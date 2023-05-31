# Jesus Carlos Martinez Gonzalez
# 30/05/2023
# Designer Door Mat (https://www.hackerrank.com/challenges/designer-door-mat/problem)

"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NxM. (N is an odd natural number, and M is 3 times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""

if __name__ == "__main__":
    n, m = map(int, input().split())
    c = ".|."
    for i in range(1, n + 1):
        if i < (n // 2 + 1):
            print((c * ((i * 2) - 1)).center(m, "-"))
        elif i > (n // 2 + 1):
            print((c * (((n - i + 1) * 2) - 1)).center(m, "-"))
        else:
            print("WELCOME".center(m, "-"))
