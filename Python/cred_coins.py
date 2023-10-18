# Jesus Carlos Martinez Gonzalez
# 17/10/2023
# CRED coins (https://www.codechef.com/problems/CREDCOINS)

"""
For each bill you pay using CRED, you earn X CRED coins.
At CodeChef store, each bag is worth 100 CRED coins.
Chef pays Y number of bills using CRED. Find the maximum number of bags he can get from the
CodeChef store.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print((a * b) // 100)
