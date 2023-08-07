# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Parity (https://www.codechef.com/problems/PAR2)

"""
Ashu and Arvind participated in a coding contest, as a result of which they received N chocolates. Now
they want to divide the chocolates between them equally.
Can you help them by deciding if it is possible for them to divide all the N chocolates in such a way that
they each get an equal number of chocolates?
You cannot break a chocolate in two or more pieces.
"""

t = int(input())
for _ in range(t):
    print("YES" if int(input()) % 2 == 0 else "NO")
