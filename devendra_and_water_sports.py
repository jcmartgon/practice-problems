# Jesus Carlos Martinez Gonzalez
# 03/12/2023
# Devendra and water sports (https://www.codechef.com/problems/DEVSPORTS)

"""
Recently, Devendra went to Goa with his friends. Devendra is well known for not following a budget.
He had Rs. Z at the start of the trip and has already spent RS. Y on the trip. There are three kinds of
water sports one can enjoy, with prices Rs. A, B, and C. He wants to try each sport at least once.
If he can try all of them at least once output YES. otherwise output NO.
"""

for _ in range(int(input())):
    budget, spent, a, b, c = map(int, input().split())

    remaining = budget - spent

    print("YES" if remaining >= a + b + c else "NO")
