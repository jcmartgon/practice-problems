# Jesus Carlos Martinez Gonzalez
# 04/08/2023
# Puzzle hunt (https://www.codechef.com/problems/PUZHUNT)

"""
Print the answer. Yes if Chefs team is eligible to participate, and No otherwise.
Each letter in the output may be printed in either uppercase or lowercase, i.e. the outputs NO, No, no. no
will all be treated as equivalent.
"""

print("YES" if int(input()) in range(6, 9) else "NO")
