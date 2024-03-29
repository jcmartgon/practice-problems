# Jesus Carlos Martinez Gonzalez
# 08/11/2023
# Self defence training (https://www.codechef.com/problems/SELFDEF)

"""
After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th
Chamber of Shaolin. The aim this time is to equip women with shaolin self-defence techniques.
The only condition for a woman to be eligible for the special training is that she must be between 10
and 60 years of age, inclusive of both 10 and 60.
Given the ages of N women in his village. please help San Te find out how many of them are eligible for
the special training.
"""

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    print(sum(1 for x in lst if x in range(10, 61)))
