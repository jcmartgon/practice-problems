# Jesus Carlos Martinez Gonzalez
# 15/03/2024
# Lucky four (https://www.codechef.com/problems/LUCKYFR)

"""
Karan likes the number 4 very much.
Impressed by the power of this number, Karan has begun to look for occurrences of four anywhere. He
has a list of T integers, for each of them he wants to calculate the number of occurrences of the digit 4
in the decimal representation. He is too busy now, so please help him.
"""

for _ in range(int(input())):
    number = input()

    print(number.count("4"))
