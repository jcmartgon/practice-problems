# Jesus Carlos Martinez Gonzalez
# 02/01/2024
# Chef and batter (https://www.codechef.com/problems/FIFTYPE)

"""
Chefs phone has a battery level of N percent.
Each minute:
• Ifthe phone is on charging. the battery level increases by 2%.
• Otherwise, the battery level decreases by 3%.
Find the minimum time in which Chef can make the battery level reach exactly 50%.
Note that the battery level should always lie in the range 0 to 100 (both included).
"""

for _ in range(int(input())):
    charge = int(input())
    minutes = 0

    while charge != 50:
        if charge > 50:
            q, r = divmod(charge - 50, 3)

            if r:
                q += 1

            charge -= 3 * q
        else:
            q, r = divmod(50 - charge, 2)

            if r:
                q += 1

            charge += 2 * q

        minutes += q

    print(minutes)
