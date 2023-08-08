# Jesus Carlos Martinez Gonzalez
# 07/08/2023
# Right there (https://www.codechef.com/problems/RIGHTTHERE)

"""
If you wanna party, if you, if you wanna party
Then put your hands up
Chef wants to host a party with a total of N people.
However, the party hall has a capacity of X people. Find whether Chef can host the party.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print("YES" if y >= x else "NO")
