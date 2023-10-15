# Jesus Carlos Martinez Gonzalez
# 14/10/2023
# Janmansh and coins (https://www.codechef.com/problems/JCOINS)

"""
Janmansh received X coins of 10 rupees and Y coins of 5 rupees from Chingari. Since he is weak in
math, can you find out how much total money does he have?
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a * 10 + b * 5)
