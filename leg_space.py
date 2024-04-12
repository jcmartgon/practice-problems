# Jesus Carlos Martinez Gonzalez
# 11/04/2024
# Leg space (https://www.codechef.com/problems/LEGSP)

"""
There are N students including Chef in a school. The school bus has M seats, and every student in the
school travels on the bus.
It is guaranteed that N < M, so that everyone will have a seat.
Chef is happy when the school bus is notfull.
Given N and M, your task is to find out whether Chef will be happy.
"""

students, seats = map(int, input().split())

print("YES" if students != seats else "NO")
