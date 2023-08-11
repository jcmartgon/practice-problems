# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Chef gives party (https://www.codechef.com/problems/PARTY2)

"""
Chef wants to give a burger party to all his N friends i.e. he wants to buy one burger for each of his
friends.
The cost of each burger is X rupees while Chef has a total of K rupees.
Determine whether he has enough money to buy a burger for each of his friends or not.
"""

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print("YES" if z >= x * y else "NO")
