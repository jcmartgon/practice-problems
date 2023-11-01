# Jesus Carlos Martinez Gonzalez
# 01/09/2023
# Test score (https://www.codechef.com/problems/CHEFSCORE)

"""
In a test, there are N problems, each carrying X marks.
In each problem, Chef either received X marks or 0 marks.
Determine whether is it possible for Chef to achieve exactly Y marks.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a * b >= c and c % b == 0 else "NO")
