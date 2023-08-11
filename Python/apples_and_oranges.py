# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Apples and oranges (https://www.codechef.com/problems/APPLORNG)

"""
Bob has X rupees and goes to a market. The cost of apples is Rs. A per kg and the cost of oranges is
Rs. B per kg.
Determine whether he can buy at least 1 kg each of apples and oranges.
"""

x = int(input())
y, z = map(int, input().split())

print("YES" if x >= y + z else "NO")
