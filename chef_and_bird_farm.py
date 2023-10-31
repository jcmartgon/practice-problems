# Jesus Carlos Martinez Gonzalez
# 31/10/2023
# Chef and bird farm (https://www.codechef.com/problems/BIRDFARM)

"""
In Chefland. each chicken has X legs and each duck has Y legs. Chefs farm can have exactly one
type of bird.
Given that the birds on the farm have a total of Z legs:
- Print CHICKEN, if the farm can have only chickens but not ducks.
- Print DUCK. if the farm can have only ducks but not chickens.
- Print ANY, if the farm can have either chickens or ducks.
- Print NONE, if the farm can have neither chickens nor ducks.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if c % a == 0 and c % b == 0:
        print("ANY")
    elif c % a == 0:
        print("CHICKEN")
    elif c % b == 0:
        print("DUCK")
    else:
        print("NONE")
