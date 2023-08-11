# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Sum it (https://www.codechef.com/problems/SUMM)

"""
Bob received an assignment from his school: he has two numbers A and B. and he has to find the sum
of these two numbers.
Alice, being a good friend of Bob, told him that the answer to this question is C.
Bob doesn't completely trust Alice and asked you to tell him if the answer given by Alice is correct or
not.
Ifthe answer is correct print "YES", otherwise print "NO" (without quotes).
"""

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print("YES" if x + y == z else "NO")
