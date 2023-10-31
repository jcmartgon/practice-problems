# Jesus Carlos Martinez Gonzalez
# 31/10/2023
# Sasta shark tank (https://www.codechef.com/problems/SST)

"""
Devendra just had a million-dollar idea and he needs funds to startup. He was recently invited to Sasta
Shark Tank (A TV show where entrepreneurs pitch their ideas to investors hoping to get investment in
return).
He was offered deals from two investors. The first investor offers A dollars for 10% of his company and
the second investor offers B dollars for 20% of his company. Devendra will accept the offer from the
investor whose valuation of the company is more. Determine which offer will Devendra accept or if
both the offers are equally good.
For example, if the first investor offers 300 dollars for 10% of the company, then the first investor's
valuation of the company is 3000 dollars since 10% of 3000 = 300. If the second investor offers 500
dollars for 20% of the company. then the second investors valuation of the company is 2500 dollars
since of 2500 = 500.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    a *= 10
    b *= 5
    if a > b:
        print("FIRST")
    elif b > a:
        print("SECOND")

    else:
        print("ANY")
