# Jesus Carlos Martinez Gonzalez
# 15/04/2024
# Worth of a video (https://www.codechef.com/problems/VIDEOWORTH)

"""
We know that "A picture is worth a thousand words". So let's calculate the worth of a video using this!
Suppose a video has 24 frames (or pictures) per second, and has a duration of S seconds. We know
that each frame is worth 1000 words. So. how many words is this video worth in total?
"""

for _ in range(int(input())):
    print(int(input()) * 24000)
