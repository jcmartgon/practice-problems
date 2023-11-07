# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# It is my serve (https://www.codechef.com/problems/MYSERVE)

"""
Alice and Bob are playing a game of table tennis where irrespective of the point scored, every player
makes 2 consecutive serves before the service changes. Alice makes the first serve of the match.
Therefore the first 2 serves will be made by Alice, then the next 2 serves will be made by Bob and so
on.
Let's consider the following example match for more clarity:

- Alice makes the ISt serve.
- Let us assume. Bob wins this point. (Score is 0 for Alice and 1 for Bob)
- Alice makes the 2nd serve.
- Let us assume, Alice wins this point. (Score is 1 for Alice and 1 for Bob)
- Bob makes the 3rd serve.
- Let us assume, Alice wins this point. (Score is 2 for Alice and 1 for Bob)
- Bob makes the 4th serve.
- Let us assume. Alice wins this point. (Score is 3 for Alice and 1 for Bob)
- Alice makes the 5th serve.
- And the game continues ...

After the score reaches P and Qfor Alice and Bob respectively, both the players forgot whose serve it
is. Help them determine whose service it is.
"""

for _ in range(int(input())):
    print("Alice" if sum(list(map(int, input().split()))) % 4 in [0, 1] else "Bob")
