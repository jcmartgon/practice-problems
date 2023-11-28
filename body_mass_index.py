# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Body mass index (https://www.codechef.com/problems/BMI)

"""
You are given the height H (in metres) and mass M (in kilograms) of Chef. The Body Mass Index (BMI)
of a person is computed as
Report the category into which Chef falls, based on his BMI:
•
•
•
•
Category 1: Underweight if BMI 18
Category 2: Normal weight if BMI e {19, 20,.. 24}
Category 3: Overweight if BMI e {25, 26... .. 29}
Category 4: Obesity if BMI 30
"""


for _ in range(int(input())):
    mass, height = map(int, input().split())

    bmi = mass / pow(height, 2)
    print(1 if bmi <= 18 else 2 if 19 <= bmi <= 24 else 3 if 25 <= bmi <= 29 else 4)
