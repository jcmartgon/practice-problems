# Jesus Carlos Martinez Gonzalez
# 03/07/2023
# Merge the Tools! (https://www.hackerrank.com/challenges/merge-the-tools/problem)

"""
Consider the following:

A string, s, of length n where s = c0c1...cn-1.
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each substring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in t occurs at a previous index < j  in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line i denotes string ui.
"""


def merge_the_tools(string, k):
    for _ in range(len(string) // k):
        sub = string[:k]
        unique = []

        for c in sub:
            if c not in unique:
                unique.append(c)

        string = string[k:]
        print("".join(unique))


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
