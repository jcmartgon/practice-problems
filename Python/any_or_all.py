# Jesus Carlos Martinez Gonzalez
# 22/06/2023
# Any or All

"""
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""


def check_palindromic_integers(numbers):
    # Convert the space-separated string of numbers to a list of integers
    num_list = list(map(int, numbers.split()))

    # Check if all numbers are positive
    if all(num > 0 for num in num_list):
        # Check if any number is palindromic
        for num in num_list:
            if is_palindromic_integer(num):
                return True

    return False


def is_palindromic_integer(num):
    # Convert the integer to a string
    num_str = str(num)

    # Compare the string with its reverse
    return num_str == num_str[::-1]


if __name__ == "__main__":
    n = int(input())
    number_list = list(map(int, input().split()))
    if check_palindromic_integers(number_list):
        print(True)
    else:
        print(False)
