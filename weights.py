# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# Weights (https://www.codechef.com/problems/WGHTS)

"""
Chef is playing with weights. He has an object weighing W units. He also has three weights each of
X, Y, and Z units respectively. Help him determine whether he can measure the exact weight of the
object with one or more of these weights.
If it is possible to measure the weight of object with one or more of these weights, print YES, otherwise
print NO.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(
        "YES"
        if b == a
        or c == a
        or d == a
        or b + c == a
        or c + d == a
        or b + d == a
        or b + c + d == a
        else "NO"
    )
