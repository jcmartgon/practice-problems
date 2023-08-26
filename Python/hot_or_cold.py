# Jesus Carlos Martinez Gonzalez
# 25/08/2023
# Is it hot or cold (https://www.codechef.com/problems/HOTCOLD)

"""
Chef considers the climate HOT if the temperature is above 20, otherwise he considers it COLD. You are
given the temperature C, find whether the climate is HOT or COLD.
"""

for _ in range(int(input())):
    print("HOT" if int(input()) > 20 else "COLD")
