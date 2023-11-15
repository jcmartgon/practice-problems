# Jesus Carlos Martinez Gonzalez
# 15/11/2023
# Packing books (https://www.codechef.com/problems/BOOKPACK)

"""
Chef is moving to a new house!
Unfortunately, this means he now has to pack up his things so that they can be moved too. Currently,
Chefis packing up his (rather impressive) book collection into cardboard boxes.
Chef has X shelves of books, each of which contains exactly Y books. Each cardboard box can hold at
most Z books. In order to not mess up the organization of the books, Chef will also ensure that books
from different shelves will not be placed in the same box.
Under these conditions, what is the minimum number of boxes needed to pack all the books?
"""


from math import ceil

for _ in range(int(input())):
    shelves, books_per_shelf, books_per_box = map(int, input().split())

    boxes_per_shelf = ceil(books_per_shelf / books_per_box)

    print(boxes_per_shelf * shelves)
