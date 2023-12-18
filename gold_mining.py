# Jesus Carlos Martinez Gonzalez
# 17/12/2023
# Gold mining (https://www.codechef.com/problems/CARRYGOLD)

"""
Chef has decided to go to a gold mine along with N of his friends (thus, total N + 1 people including
Chef go to the gold mine).
The gold mine contains a total of X kg of gold. Every person has the capacity of carrying up atmost
Y kg of gold.
Will Chef and his friends together be able to carry up all the gold from the gold mine assuming that
they can go to the mine exactly once.
"""

for _ in range(int(input())):
    people, total_gold, gold_per_person = map(int, input().split())

    print("YES" if (people + 1) * gold_per_person >= total_gold else "NO")
