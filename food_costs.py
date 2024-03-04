# Jesus Carlos Martinez Gonzalez
# 03/03/2024
# Food costs (https://www.codechef.com/problems/FOODCOST)

"""
You're a bit all over the place as a college student. You used to eat out at expensive restaurants almost
every day until your parents gave you a talking-to about being irresponsible. Now, you've got to control
your eating and spending habits.
So, here's the plan: you'll stick to the college mess for your meals every day, except Sundays. on
Sundays, you're treating yourself to those fancy restaurant meals.
The cost is Rs. X for the mess food each day, and Rs. Y for the restaurant splurges.
Now, what's the cost of food per week? Note that you don't have to pay for the mess on Sundays.
A week has seven days, as usual.
"""

mess, fancy = map(int, input().split())

print(6 * mess + fancy)
