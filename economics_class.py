# Jesus Carlos Martinez Gonzalez
# 18/11/2023
# Economic class (https://www.codechef.com/problems/ECOCLASS)

"""
Alice has recently learned in her economics class that the market is said to be in equilibrium when the
supply is equal to the demand.
Alice has market data for N time points in the form of two integer arrays S and D. Here, Si denotes
the supply at the point of time and Di denotes the demand at the point of time, for each 1
i<N.
Help Alice in finding out the number of time points at which the market was in equilibrium.
"""


for _ in range(int(input())):
    n = int(input())
    supply = [int(x) for x in input().split()]
    demand = [int(x) for x in input().split()]

    print(sum(1 for x, y in zip(supply, demand) if x == y))
