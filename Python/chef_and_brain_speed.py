# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Chef and brain speed (https://www.codechef.com/problems/CBSPEED)

"""
In ChefLand, human brain speed is measured in bits per second (bps). Chef has a threshold limit of X
bits per second above which his calculations are prone to errors. If Chef is currently working at Y bits
per second. is he prone to errors?
If Chef is prone to errors print YES, otherwise print NO.
"""

x, y = map(int, input().split())
print("YES" if x < y else "NO")
