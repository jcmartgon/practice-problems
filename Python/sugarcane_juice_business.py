# Jesus Carlos Martinez Gonzalez
# 24/10/2023
# Sugarcane juice business (https://www.codechef.com/problems/SUGARCANE)

"""
While Alice was drinking sugarcane juice, she started wondering about the following facts:
• The juicer sells each glass of sugarcane juice for 50 coins.
• He spends 20% of his total income on buying sugarcane.
• He spends 20% of his total income on buying salt and mint leaves.
• He spends 30% of his total income on shop rent.
Alice wonders, what is the juicer's profit (in coins) when he sells N glasses of sugarcane juice?
"""

for _ in range(int(input())):
    x = int(input())
    print((x * 50) - (x * 20 + x * 15))
