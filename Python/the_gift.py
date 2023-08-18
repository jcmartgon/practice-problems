# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# The gift (https://www.codechef.com/problems/CS2023_GIFT)

"""
Om has X rupees. He wants to gift a laptop worth N rupees to his girlfriend.
We know that Om is the technical secretary of IIIT-A and has access to the Gymkhana funds of IIIT-A.
Currently there are M rupees in the fund and Om can use the fund as much as he wants.
Find whether Om can gift his girlfriend a new laptop.
"""

x, n, m = map(int, input().split())
print("YES" if x + m >= n else "NO")
