# Jesus Carlos Martinez Gonzalez
# 22/10/2023
# Expert setter (https://www.codechef.com/problems/EXPERT)

"""
A problem setter is called an expert if at least 50% of their problems are approved by Chef.
Munchy submitted X problems for approval. If Y problems out of those were approved, find whether
Munchy is an expert or not.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if b / a >= 0.5 else "NO")
