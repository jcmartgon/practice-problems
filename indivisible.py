# Jesus Carlos Martinez Gonzalez
# 18/11/2023
# Indivisible (https://www.codechef.com/problems/INDIVISIBLE)

"""
Alice thinks Bob has very weak math skills.
Alice gave Bob three numbers A, B, and C and challenged him to find any positive integer K strictly
less than 100 such that none of the three numbers are divisible by K.
Help Bob find one such integer K. Note that there can be multiple correct values for K, you need to
output just one.
Under the given constraints. a valid K will always exist.
"""


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    for i in range(2, 100):
        if a % i != 0 and b % i != 0 and c % i != 0:
            print(i)
            break
