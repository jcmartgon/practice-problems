# Jesus Carlos Martinez Gonzalez
# 20/11/2023
# Degree of polynomial (https://www.codechef.com/problems/DPOLY)

"""
In mathematics, the degree of polynomials in one variable is the highest power of the variable in the
algebraic expression with non-zero coefficient.
Chef has a polynomial in one variable twith N terms. The polynomial looks like Ao • + A1 • cl +
... + AN—2 • cN¯2 + AN—I • cN¯l where Ai—I denotes the coefficient of the term xi¯l for all
Find the degree of the polynomial.
Note: It is guaranteed that there exists at least one term with non-zero coefficient.
"""


for _ in range(int(input())):
    n = int(input())
    poly = [int(x) for x in input().split()]

    for x in reversed(poly):
        if x != 0:
            break
        n -= 1

    print(n - 1)
