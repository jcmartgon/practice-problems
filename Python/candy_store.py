# Jesus Carlos Martinez Gonzalez
# 24/08/2023
# Candy store (https://www.codechef.com/problems/CANDYSTORE)

"""
Chef has started working at the candy store. The store has 100 chocolates in total.
Chefs daily goal is to sell X chocolates. For each chocolate sold, he will get 1 rupee. However, if Chef
exceeds his daily goal, he gets 2 rupees per chocolate for each extra chocolate.
If Chef sells Y chocolates in a day. find the total amount he made.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = b - a if b - a > 0 else 0
    print(a + 2 * c if b >= a else b)
