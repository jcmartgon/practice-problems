# Jesus Carlos Martinez Gonzalez
# 04/09/2023
# Mario and transformation (https://www.codechef.com/problems/TRANSFORM)

"""
Mario transforms each time he eats a mushroom as follows:
• If he is currently small, he turns normal.
• If he is currently normal, he turns huge.
• If he is currently huge, he turns small.
Given that Mario was initially normal, find his size after eating X mushrooms.
"""

for _ in range(int(input())):
    x = int(input())
    lst = ["NORMAL", "HUGE", "SMALL"]
    print(lst[x % 3])
