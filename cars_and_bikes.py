# Jesus Carlos Martinez Gonzalez
# 23/11/2023
# Cars and bikes (https://www.codechef.com/problems/TYRES)

"""
Chef opened a company which manufactures cars and bikes. Each car requires 4 tyres while each bike
requires 2 tyres. Chef has a total of N tyres (N is even). He wants to manufacture maximum number of
cars from these tyres and then manufacture bikes from the remaining tyres.
Chef's friend went to Chef to purchase a bike. If Chef's company has manufactured even a single bike
then Chefs friend will be able to purchase it.
Determine whether he will be able to purchase the bike or not.
"""


for _ in range(int(input())):
    tyres = int(input())

    for_bikes = tyres - (tyres // 4) * 4

    print("YES" if for_bikes % 2 == 0 and for_bikes != 0 else "NO")
