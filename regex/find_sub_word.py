# Jesus Carlos Martinez Gonzalez
# 28/05/2023
# Find a sub-word (https://www.hackerrank.com/challenges/find-substring/problem)

"""
Given n sentences consisting of one or more words separated by non-word characters, process q queries where each query consists of a single string, s. 
To process each query, count the number of occurrences of  as a sub-word in all n sentences, then print the number of occurrences on a new line.
"""

import re

if __name__ == "__main__":
    text = ""
    n = int(input())
    for _ in range(n):
        text += input() + " "
    q = int(input())
    for _ in range(q):
        sub = input()
        matches = re.findall(rf"(?<=\w){sub}(?=\w)", text)
        print(len(matches))
