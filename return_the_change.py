# Jesus Carlos Martinez Gonzalez
# 14/11/2023
# Return the change (https://www.codechef.com/problems/RETURNCHANGE)

"""
In Chefland, denominations less than rupees 10 have stopped and now rupees IO is the smallest
denomination.
Suppose Chef goes to buy some item with cost not a multiple of 10, then, he will be charged the cost
that is the nearest multiple of 10.
If the cost is equally distant from two nearest multiples of 10, then the cost is rounded up.
For example, 35, 38, 40, 44 are all rounded to 40.
Chef purchased an item having cost X (X 100) and gave a bill of rupees 100. How much amount
will he get back?
"""


for _ in range(int(input())):
    print(100 - round(int(input()), -1))
