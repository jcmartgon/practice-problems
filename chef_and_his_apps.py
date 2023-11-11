# Jesus Carlos Martinez Gonzalez
# 08/11/2023
# Chef and his apps (https://www.codechef.com/problems/CHEFAPPS)

"""
Chef's phone has a total storage of S MB. Also, Chef has 2 apps already installed on his phone which
occupy X MB and Y MB respectively.
He wants to install another app on his phone whose memory requirement is Z MB. For this, he might
have to delete the apps already installed on his phone. Determine the minimum number of apps he
has to delete from his phone so that he has enough memory to install the third app.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    available = a - (b + c)
    counter = 0

    if d > available:
        available += max(b, c)
        counter += 1

    if d > available:
        available += min(b, c)
        counter += 1

    print(counter)
