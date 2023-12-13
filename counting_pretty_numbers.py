# Jesus Carlos Martinez Gonzalez
# 12/12/2023
# Counting pretty numbers (https://www.codechef.com/problems/NUM239)

"""
Vasya likes the number 239. Therefore, he considers a number prettyif its last digit is 2, 3 or 9.
Vasya wants to watch the numbers between L and R (both inclusive), so he asked you to determine
how many pretty numbers are in this range. Can you help him?
"""

for _ in range(int(input())):
    start, finish = map(int, input().split())

    pretty = 0
    for i in range(start, finish + 1):
        q, r = divmod(i, 10)

        if r in [2, 3, 9]:
            pretty += 1

    print(pretty)
