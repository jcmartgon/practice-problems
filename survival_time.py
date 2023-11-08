# Jesus Carlos Martinez Gonzalez
# 08/09/2023
# Survival time (https://www.codechef.com/problems/FIZZBUZZ23_2)

"""
The apocalypse has arrived, and Alice and her 4 other family members (a total of 5 people) are now
stuck in a shopping mall from where they have nowhere to run.
Fortunately, the place where they are stuck has frozen buns which they can eat and survive.
There are N buns in the mall, and each member of the family needs to eat X buns everyday to survive.
After the food supply runs out, the family can survive for a further D days.
How many days can Alice and family survive under these conditions?
Note: If there aren't enough buns to feed the whole family, nobody will eat anything. The samples
below showcase an example of this.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a // (b * 5) + c)
