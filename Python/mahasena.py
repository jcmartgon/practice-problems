# Jesus Carlos Martinez Gonzalez
# 16/10/2023
# Mahasena (https://www.codechef.com/problems/AMR15A)

"""
Kattapa, as you all know was one of the greatest warriors of his time. The kingdom of Maahishmati had
never lost a battle under him (as army-chief), and the reason for that was their really powerful army,
also called as Mahasena.
Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier
is holding an even number of weapons, and "unlucky" otherwise. He considered the army as "READY
FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and
"NOT READY" otherwise.
Given the number of weapons each soldier is holding, your task is to determine whether the army
formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".
"""

n = int(input())
lst = list(map(int, input().split()))
even = odd = 0
for x in lst:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("READY FOR BATTLE" if even > odd else "NOT READY")
