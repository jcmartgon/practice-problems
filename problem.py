# Jesus Carlos Martinez Gonzalez
# 26/02/2024
# Problem (https://www.codechef.com/problems/PR0BLEM)

"""
One less problem without ya
I got one less problem without ya
Alice and Bob are competing in a challenge. Initially Alice has N problems and Bob has M problems.
• Each time Alice solves a problem, Bob receives one more problem to solve.
• Each time Bob solves a problem, Alice receives three more problems to solve.
Find whether it is possible that both of them have the same number of problems left if they can solve
the problems in any arbitrary manner.
"""

for _ in range(int(input())):
    alice, bob = map(int, input().split())
    print("YES" if abs(alice - bob) % 2 == 0 else "NO")
