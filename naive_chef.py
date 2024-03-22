# Jesus Carlos Martinez Gonzalez
# 21/03/2024
# Naive chef (https://www.codechef.com/problems/NAICHEF?tab=statement)

"""
Once, after a stressful day, Chef decided to relax and visit a casino near his house to gamble. He feels
lucky and he's going to bet almost all of his money.
The game Chef is going to play in the casino consists of tossing a die with N faces twice. There is a
number written on each face of the die (these numbers are not necessarily distinct). In order to win,
Chef must get the number A on the first toss and the number B on the second toss of the die.
The excited viewers want to know the probability that Chef will win the game. Can you help them find
that number? Assume that Chef gets each face of the die with the same probability on each toss and
that tosses are mutually independent.
"""

for _ in range(int(input())):
    n, a, b = input().split()
    n = int(n)
    dice = input()

    prob_a = dice.count(a) / n
    prob_b = dice.count(b) / n
    prob = format((prob_a * prob_b), ".10f")

    print(prob)
