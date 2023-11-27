# Jesus Carlos Martinez Gonzalez
# 26/11/2023
# The block game (https://www.codechef.com/problems/PALL01)

"""
The citizens of Byteland regularly play a game. They have blocks each denoting some integer from O to
9. These are arranged together in a random manner without seeing to form different numbers keeping
in mind that the first block is never a O. Once they form a number they read in the reverse order to
check if the number and its reverse is the same. If both are same then the player wins. We call such
numbers palindrome.
Ash happens to see this game and wants to simulate the same in the computer. As the first step he
wants to take an input from the user and check if the number is a palindrome and declare if the user
wins or not.
"""


for _ in range(int(input())):
    n = input()
    l = len(n)
    valid = True

    if n[0] != "0":
        for i in range(l // 2):
            if n[i] != n[l - 1 - i]:
                valid = False
    else:
        valid = False

    print("wins" if valid else "loses")
