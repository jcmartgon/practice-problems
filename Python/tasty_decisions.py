# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Tasty decisions (https://www.codechef.com/problems/TASTEDEC)

"""
Chef is buying sweet things to prepare for Halloween!
The shop sells both chocolate and candy.
• Each bar of chocolate has a tastiness of X.
• Each piece of candy has a tastiness of Y.
One packet of chocolate contains 2 bars, while one packet of candy contains 5 pieces.
Chef can only buy one packet of something sweet, and so has to make a decision: which one should he
buy in order to maximize the total tastiness of his purchase?
Print Chocolate if the packet of chocolate is tastier, candy if the packet of candy is tastier, and Either if
they have the same tastiness.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    x = x * 2
    y = y * 5

    if x > y:
        print("CHOCOLATE")
    elif y > x:
        print("CANDY")
    else:
        print("EITHER")
