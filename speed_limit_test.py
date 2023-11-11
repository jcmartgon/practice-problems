# Jesus Carlos Martinez Gonzalez
# 09/11/2023
# Speed limit test (https://www.codechef.com/problems/SPEEDTEST)

"""
Alice is driving from her home to her office which is A kilometers away and will take her X hours to
reach.
Bob is driving from his home to his office which is B kilometers away and will take him Y hours to
reach.
Determine who is driving faster, else, if they are both driving at the same speed print EQUAL.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    alice = a / b
    bob = c / d

    print("Alice" if alice > bob else "Bob" if bob > alice else "Equal")
