# Jesus Carlos Martinez Gonzalez
# 02/06/2023
# DefaultDict tutorial (https://www.hackerrank.com/challenges/defaultdict-tutorial/problem)

"""
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. 
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.
"""

from collections import defaultdict


if __name__ == "__main__":
    a = defaultdict(list)
    a_size, b_size = map(int, input().split())
    for i in range(1, a_size + 1):
        key = input()
        a[key].append(i)
    for _ in range(b_size):
        key = input()
        print(*(a[key] if key in a else [-1]), sep=" ")
