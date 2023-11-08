# Jesus Carlos Martinez Gonzalez
# 08/09/2023
# Cup finals (https://www.codechef.com/problems/CRICUP)

"""
It is the World Cup Finals. Chef only finds a match interesting if the skill difference of the competing
teams is less than or equal to D.
Given that the skills ofthe teams competing in the final are X and Y respectively, determine whether
Chef will find the game interesting or not.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if abs(a - b) <= c else "NO")
