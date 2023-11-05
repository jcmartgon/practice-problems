# Jesus Carlos Martinez Gonzalez
# 04/09/2023
# Sunday brunch (https://www.codechef.com/problems/BRUNCH)

"""
On a sunny Sunday afternoon, Chef prepared a brunch for his 20 neighbours.
Chef prepared a total of X plates. However, the meal was so good that the neighbours started taking
Y plates each.
Find the maximum number of neighbours Chef can feed completely.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(min(a // b, 20))
