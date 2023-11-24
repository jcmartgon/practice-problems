# Jesus Carlos Martinez Gonzalez
# 23/11/2023
# Wordle (https://www.codechef.com/problems/WORDLE)

"""
Chef invented a modified wordle.
There is a hidden word S and a guess word T, both of length 5.
Chef defines a string M to determine the correctness of the guess word. For the t index:
• Ifthe guess at the index is correct, the character of M is G.
• Ifthe guess at the index is wrong, the character of M is B.
Given the hidden word S and guess T, determine string M.
"""


for _ in range(int(input())):
    hidden = input()
    guess = input()
    output = ""

    for i in range(len(hidden)):
        if hidden[i] == guess[i]:
            output += "G"
        else:
            output += "B"

    print(output)
