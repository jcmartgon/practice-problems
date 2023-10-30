# Jesus Carlos Martinez Gonzalez
# 29/10/2023
# Air conditioner temperature (https://www.codechef.com/problems/ACTEMP)

"""
There are three people sitting in a room - Alice, Bob, and Charlie. They need to decide on the
temperature to set on the air conditioner. Everyone has a demand each:
• Alice wants the temperature to be at least A degrees.
• Bob wants the temperature to be at most B degrees.
• Charlie wants the temperature to be at least C degrees.
Can they all agree on some temperature, or not?
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if b - max(a, c) >= 0 else "NO")
