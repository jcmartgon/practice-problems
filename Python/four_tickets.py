# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Four tickets (https://www.codechef.com/problems/FOURTICKETS)

"""
Four friends want to attend a concert. Each ticket costs X rupees.
They have decided to go to the concert if and only if the total cost of the tickets does not exceed 1000
rupees.
Determine whether they will be going to the concert or not.
"""

for _ in range(int(input())):
    print("YES" if int(input()) * 4 <= 1000 else "NO")
