# Jesus Carlos Martinez Gonzalez
# 01/12/2023
# Ambiguous permutations (https://www.codechef.com/problems/PERMUT2)

"""
Some programming contest problems are really tricky: not only do they require a different output
format from what you might have expected, but also the sample output does not show the difference.
For an example, let us look at permutations.
A permutation of the integers 1 to n is an ordering of these integers. So the natural way to represent a
permutation is to list the integers in this order. With n = 5, a permutation might look like 2, 3, 4, 5, I.
However, there is another possibility of representing a permutation: You create a list of numbers where
the i-th number is the position of the integer i in the permutation. Let us call this second possibility an
inverse permutation. The inverse permutation for the sequence above is 5, 1, 2, 3.4.
An ambiguous permutation is a permutation which cannot be distinguished from its inverse
permutation. The permutation 1, 4, 3, 2 for example is ambiguous, because its inverse permutation is
the same. To get rid of such annoying sample test cases, you have to write a program which detects if a
given permutation is ambiguous or not.
"""

n = int(input())
while n != 0:
    permutation = [int(x) for x in input().split()]

    inverse = [None] * len(permutation)
    for i, x in enumerate(permutation):
        inverse[x - 1] = i + 1

    print("ambiguous" if permutation == inverse else "not ambiguous")
    n = int(input())
