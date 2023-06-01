# Jesus Carlos Martinez Gonzalez
# 31/05/2023
# Alphabet Rangoli (https://www.hackerrank.com/challenges/alphabet-rangoli/problem)

"""
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
"""


def print_rangoli(size):
    """Prints an ascii rangoli of 2 * size - 1 rows"""

    # List of all lower-case letters
    az = list(map(chr, range(97, 123)))

    # List of letters to use for ragnoli, in order
    letters = az[size - 1 :: -1] + az[1:size]

    # Ragnoli's width
    width = len("-".join(letters))

    # First half
    for i in range(1, size):
        print(
            "-".join(az[size - 1 : size - i : -1] + az[size - i : size]).center(
                width, "-"
            )
        )

    # Second half
    for i in range(size, 0, -1):
        print(
            "-".join(az[size - 1 : size - i : -1] + az[size - i : size]).center(
                width, "-"
            )
        )


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
