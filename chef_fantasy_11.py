# Jesus Carlos Martinez Gonzalez
# 12/11/2023
# Chef fantasy (https://www.codechef.com/problems/FIZZBUZZ2303)

"""
All of Chefs friends are playing fantasy cricket based upon the ODI World Cup, and Chef would like to
join them.
For a certain cricket match, Chef has decided upon his team of 11 players. However, he hasn't yet
decided who should be the captain and who should be the vice-captain.
He's narrowed his decision down to N players out of the 11, from which he'll choose one to be the
captain and one to be the vice captain.
How many different choices does he have?
"""

for _ in range(int(input())):
    n = int(input())
    print(n * (n - 1))
