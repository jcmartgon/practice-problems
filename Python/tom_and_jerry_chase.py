# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Tom and jerry chase (https://www.codechef.com/problems/JERRYCHASE)

"""
In a classic chase, Tom is running after Jerry as Jerry has eaten Tom's favourite food.
Jerry is running at a speed of X metres per second while Tom is chasing him at a speed of Y metres
per second. Determine whether Tom will be able to catch Jerry.
Note that initially Jerry is not at the same position as Tom.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print("YES" if y > x else "NO")
