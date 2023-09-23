# Jesus Carlos Martinez Gonzalez
# 22/09/2023
# Codechef airlines (https://www.codechef.com/problems/AIRLINES)

"""
Chef has opened a new airline. Chef has 10 airplanes where each airplane has a capacity of X
passengers.
On the first day itself, Y people are willing to book a seat in any one of Chefs airplanes.
Given that Chef charges Z rupees for each ticket. find the maximum amount he can earn on the first
day.
"""

for _ in range(int(input())):
    seats_per_plane, customers, price = map(int, input().split())
    total_seats = seats_per_plane * 10
    print(customers * price if customers <= total_seats else total_seats * price)
