# Jesus Carlos Martinez Gonzalez
# 04/09/2023
# Hackerman (https://www.codechef.com/problems/PRIMEDICE)

from is_prime import is_prime

"""
Hackerman wants to know who is the better player between Bob and Alice with the help of a game.
The game proceeds as follows:
• First. Alice throws a die and gets the number A
• Then. Bob throws a die and gets the number B
• Alice wins the game if the sum on the dice is a prime number and Bob wins otherwise.
Given A and B, determine who wins the game.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("Alice" if is_prime(a + b) else "Bob")
