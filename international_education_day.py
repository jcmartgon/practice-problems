# Jesus Carlos Martinez Gonzalez
# 2/04/2024
# International education day (https://www.codechef.com/problems/IED)

"""
On the occasion of International Education Dayr a fair is held in Chefland.
Both Chef and Chefina have set up their stalls.
Chef sells each item at his stall for A rupees and Chefina sells each item at her store for B rupees.
If both of them sell exactly C items, find the maximum amount in sales amongst Chef and Chefina.
"""

a, b, c = map(int, input().split())

print(max(a, b) * c)
