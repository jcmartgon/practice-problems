# Jesus Carlos Martinez Gonzalez
# 02/09/2023
# Bus seat numbering (https://www.codechef.com/problems/SEATNUMBER)

"""
There is a bus with 30 seats. The seats are numbered from 1 to 30, and the numbering is as depicted in
this image.

As can be seen in the image, the bus is divided into two decks - The Lower deck, and the Upper deck,
with 15 seats each. And some of the seats come as Single and some as Double. For example, Seats I
and 2 are Double, whereas Seat 11 is a Single.
You will be given a Seat number, and your job is to classify it as one of these 4 types:

- Lower Single
- Lower Double
- Upper Single
- Upper Double
"""

for _ in range(int(input())):
    x = int(input())
    if x <= 10:
        print("LOWER DOUBLE")
    elif x <= 15:
        print("LOWER SINGLE")
    elif x <= 25:
        print("UPPER DOUBLE")
    else:
        print("UPPER SINGLE")
