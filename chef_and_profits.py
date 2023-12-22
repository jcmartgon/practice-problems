# Jesus Carlos Martinez Gonzalez
# 21/12/2023
# Chef and profits (https://www.codechef.com/problems/CHFPROFIT)

"""
Some time ago, Chef bought X stocks at the cost of Rs. Y each. Today, Chef is going to sell all these X
stocks at Rs. Z each. What is Chefs total profit after he sells them?
Chef's profit equals the total amount he received by selling the stocks, minus the total amount he spent
buying them.
"""

for _ in range(int(input())):
    stocks, cost, value = map(int, input().split())

    print(stocks * value - stocks * cost)
