# Jesus Carlos Martinez Gonzalez
# 13/10/2023
# Shopping change (https://www.codechef.com/problems/SHOPCHANGE)

"""
Chef went shopping and bought items worth X rupees (I X < 100). Unfortunately, Chef only has a
single 100 rupees note.
Since Chef is weak at maths, can you help Chef in calculating what money he should get back after
paying 100 rupees for those items?
Input Format
• First line will contain T, the number of test cases. Then the test cases follow.
• Each test case consists of a single line containing an integer X. the total price of items Chef
purchased.
"""

for _ in range(int(input())):
    print(100 - int(input()))
