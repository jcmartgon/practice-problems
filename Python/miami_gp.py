# Jesus Carlos Martinez Gonzalez
# 30/09/2023
# Miami GP (https://www.codechef.com/problems/F1RULE)

"""
Chef has finally got the chance of his lifetime to drive in the Fl tournament. But. there is one problem.
Chef did not know about the 107% rule and now he is worried whether he will be allowed to race in the
main event or not.
Given the fastest finish time as X seconds and Chefs finish time as Y seconds, determine whether
Chef will be allowed to race in the main event or not.
Note that Chef will only be allowed to race if his finish time is within 107% of the fastest finish time.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if b <= a * 1.07 else "NO")
