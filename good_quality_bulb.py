# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Good quality bulb (https://www.codechef.com/problems/BULBLIFE)

"""
A bulb company claims that the average lifetime of its bulbs is at least X units.
The company ran a test on N bulbs. You are given the lifetime of N — I of these bulbs. What is the
minimum non-negative integer value of lifetime the remaining bulb can have, such that the claim of the
company holds true?
"""


for _ in range(int(input())):
    bulbs, duration = map(int, input().split())
    durations = [int(x) for x in input().split()]

    x = duration * (len(durations) + 1) - sum(durations)

    print(x if x >= 0 else 0)
