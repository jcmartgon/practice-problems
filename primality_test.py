# Jesus Carlos Martinez Gonzalez
# 20/11/2023
# Primality test (https://www.codechef.com/problems/PRB01)

"""
Alice and Bob are meeting after a long time. As usual they love to play some math games. This times
Alice takes the call and decides the game. The game is very simple, Alice says out an integer and Bob
has to say whether the number is prime or not. Bob as usual knows the logic but since Alice doesn't
give Bob much time to think, so Bob decides to write a computer program.
Help Bob accomplish this task by writing a computer program which will calculate whether the number
is prime or not .
"""


from math import sqrt

for _ in range(int(input())):
    n = int(input())
    is_prime = True

    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            is_prime = False
            print("no")
            break

    if is_prime:
        print("yes")
