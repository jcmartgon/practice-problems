# Jesus Carlos Martinez Gonzalez
# 27/11/2023
# Grade the steel (https://www.codechef.com/problems/FLOW014)

"""
A certain type of steel is graded according to the following conditions.
1. Hardness of the steel must be greater than 50
2. Carbon content of the steel must be less than 0.7
3. Tensile strength must be greater than 5600
The grades awarded are as follows:
•
•
•
•
•
•
Grade is 10 if all three conditions are met
Grade is 9 if conditions (1) and (2) are met
Grade is 8 if conditions (2) and (3) are met
Grade is 7 if conditions (1 ) and (3) are met
Grade is 6 if only one condition is met
Grade is 5 if none of the three conditions are met
Write a program to display the grade of the steel, based on the values of hardness, carbon content and
tensile strength of the steel, given by the user.
"""


for _ in range(int(input())):
    hardness, carbon_content, tensile_strength = map(float, input().split())

    hardness = hardness > 50
    carbon_content = carbon_content < 0.7
    tensile_strength = tensile_strength > 5600

    if hardness and carbon_content and tensile_strength:
        print(10)
    elif hardness and carbon_content:
        print(9)
    elif carbon_content and tensile_strength:
        print(8)
    elif hardness and tensile_strength:
        print(7)
    elif hardness or carbon_content or tensile_strength:
        print(6)
    else:
        print(5)
