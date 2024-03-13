# Jesus Carlos Martinez Gonzalez
# 12/03/2024
# Farmer and his plot (https://www.codechef.com/problems/RECTSQ)

"""
Santosh has a farm at Byteland. He has a very big family to look after. His life takes a sudden turn and
he runs into a financial crisis. After giving all the money he has in his hand, he decides to sell his plots.
The speciality of his land is that it is rectangular in nature. Santosh comes to know that he will get more
money if he sells square shaped plots. So keeping this in mind, he decides to divide his land into
minimum possible number of square plots, such that each plot has the same area, and the plots
divide the land perfectly. He does this in order to get the maximum profit out of this.
So your task is to find the minimum number of square plots with the same area. that can be
formed out of the rectangular land. such that they divide it perfectly.
"""

for _ in range(int(input())):
    length, breadth = map(int, input().split())

    gdc = min(length, breadth)

    while length % gdc != 0 or breadth % gdc != 0:
        gdc -= 1

    print(int(length * breadth / (gdc * gdc)))
