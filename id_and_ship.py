# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Id and ship (https://www.codechef.com/problems/FLOW010)

"""
Write a program that takes in a letterclass ID of a ship and display the equivalent string class
description of the given ID. Use the table below.
B or b for BattleShip
C or c for Cruiser
D or d for Destroyer
F or f for Frigate
"""


categories = {"b": "BattleShip", "c": "Cruiser", "d": "Destroyer", "f": "Frigate"}

for _ in range(int(input())):
    print(categories[input().lower()])
