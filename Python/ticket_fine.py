# Jesus Carlos Martinez Gonzalez
# 15/08/2023
# Ticket fine (https://www.codechef.com/problems/TCKTFINE)

"""
On a certain train, Chef-the ticket collector, collects a fine of Rs. X if a passenger is travelling without a
ticket. It is known that a passenger carries either a single ticket or no ticket.
P passengers are travelling and they have a total of Qtickets. Help Chef calculate the total fine
collected.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a * (b - c))
