# Jesus Carlos Martinez Gonzalez
# 31/10/2023
# Good program (https://www.codechef.com/problems/NIBBLE)

"""
In computing, the collection of four bits is called a nibble.
Chef defines a program as:
• Good. if it takes exactly X nibbles of memory, where X is a positive integer.
• Not Good, otherwise.
Given a program which takes N bits of memory, determine whether it is Good or Not Good.
"""

for _ in range(int(input())):
    print("GOOD" if int(input()) % 4 == 0 else "NOT GOOD")
