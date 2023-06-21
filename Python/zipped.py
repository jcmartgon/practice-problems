# Jesus Carlos Martinez Gonzalez
# 20/06/2023
# Zipped! (https://www.hackerrank.com/challenges/zipped/problem)

"""
This function returns a list of tuples. The ith tuple contains the ith element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.
"""

if __name__ == "__main__":
    n, x = map(int, input().split())
    marks = []
    for _ in range(x):
        marks.append(list(map(float, input().split())))
    for m in zip(*marks):
        print(sum(m) / len(m))
