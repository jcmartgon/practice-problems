# Jesus Carlos Martinez Gonzalez
# 11/03/2024
# Ceil and receipt (https://www.codechef.com/problems/CIELRCPT)

"""
Tomya is a girl. She loves Chef Ciel very much.
Tomya like a positive integer p, and now she wants to get a receipt of Ciel's restaurant whose total price
is exactly p. The current menus of Ciel's restaurant are shown the following table.

Note that the i-th menu has the price 2i-1 (I s i 12).
So please find the minimum number of menus whose total price is exactly p. Note that if she orders the
same menu twice. then it is considered as two menus are ordered. (See Explanations for details)
"""

for _ in range(int(input())):
    price = int(input())

    items = 0
    closest_price = 1

    while closest_price * 2 <= price and closest_price * 2 <= 2048:
        closest_price *= 2

    while price > 0:
        q, price = divmod(price, closest_price)
        items += q

        while price < closest_price:
            closest_price /= 2

    print(int(items))
