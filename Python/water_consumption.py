# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# Water consumption (https://www.codechef.com/problems/WATERCONS)

"""
Recently, Chef visited his doctor. The doctor advised Chef to drink at least 2000 ml of water each day. Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not.
"""

t = int(input())
for _ in range(t):
    print("YES" if int(input()) >= 2000 else "NO")
