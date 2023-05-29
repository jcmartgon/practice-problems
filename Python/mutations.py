# Jesus Carlos Martinez Gonzalez
# 28/05/2023
# Mutations (https://www.hackerrank.com/challenges/python-mutations/problem)

"""
Read a given string, change the character at a given index and then print the modified string.
"""


def mutate_string(string, position, character):
    tmp = list(string)
    tmp[position] = character
    return "".join(tmp)


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
