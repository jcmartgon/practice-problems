# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Complementary strand in a DNA (https://www.codechef.com/problems/DNASTRAND)

"""
You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S
contains the character A, T, C, and G only.
Chef knows that:
A is complementary to T.
T is complementary to A.
C is complementary to G.
• G is complementary to C.
Using the string S, determine the sequence of the complementary strand of the DNA
"""

for _ in range(int(input())):
    n = int(input())
    s = input()

    dct = {"A": "T", "T": "A", "C": "G", "G": "C"}

    print("".join(dct.get(c, c) for c in s))
