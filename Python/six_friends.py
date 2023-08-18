# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# Email reminders (https://www.codechef.com/problems/SIXFRIENDS)

"""
Six friends go on a trip and are looking for accommodation. After looking for hours, they find a hotel
which offers two types of rooms — double rooms and triple rooms. A double room costs Rs. X, while a
triple room costs Rs. Y.
The friends can either get three double rooms or get two triple rooms. Find the minimum amount they
will have to pay to accommodate all six of them.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    a *= 3
    b *= 2
    print(a if a <= b else b)
