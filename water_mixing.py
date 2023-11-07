# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# Water mixing (https://www.codechef.com/problems/WTRMIXING)

"""
Chef is setting up a perfect bath for himself. He has X litres of hot water and Y litres of cold water.
The initial temperature of water in his bathtub is A degrees. On mixing water, the temperature of the
bathtub changes as following:
• The temperature rises by 1 degree on mixing 1 litre of hot water.
• The temperature drops by 1 degree on mixing 1 litre of cold water.
Determine whether he can set the temperature to B degrees for a perfect bath.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a < b:
        print("YES" if a + c >= b else "NO")
    elif a > b:
        print("YES" if a - d <= b else "NO")
    else:
        print("YES")
