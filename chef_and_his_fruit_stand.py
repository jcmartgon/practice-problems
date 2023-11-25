# Jesus Carlos Martinez Gonzalez
# 24/11/2023
# Chef and his fruit stand (https://www.codechef.com/problems/FRUITCHAAT)

"""
Chef has closed his restaurant and decided to run a fruit stand instead. His signature dish is a fruit
chaat consisting of 2 bananas and 1 apple. He currently has X bananas and Y apples. How many
chaats can he make with the fruits he currently has?
"""


for _ in range(int(input())):
    bananas, apples = map(int, input().split())

    banana_pairs = bananas // 2

    print(banana_pairs if banana_pairs <= apples else apples)
