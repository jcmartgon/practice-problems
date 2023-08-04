# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# Chef plays ludo (https://www.codechef.com/problems/LUDO)

"""
Chef is playing Ludo. According to the rules of Ludo, a player can enter a new token into the play only when he rolls a 6 on the die. 
In the current turn, Chef rolled the number X on the die. Determine if Chef can enter a new token into the play in the current turn or not.
"""

t = int(input())
for _ in range(t):
    print("YES" if int(input()) == 6 else "NO")
