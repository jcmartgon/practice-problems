# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Tour of king (https://www.codechef.com/problems/KNGTOR)

"""
King loves to go on tours with his friends.
King has N cars that can seat 5 people each and M cars that can seat 7 people each. Determine the
maximum number of people that can travel together in these cars.
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(x * 5 + y * 7)
