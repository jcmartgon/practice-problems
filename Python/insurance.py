# Jesus Carlos Martinez Gonzalez
# 21/09/2023
# Insurance (https://www.codechef.com/problems/INSURANCE)

"""
Chef bought car insurance. The policy of the insurance is:
• The maximum rebatable amount for any damage is Rs X lakhs.
• Ifthe amount required for repairing the damage is X lakhs. that amount is rebated in full.
Chef's car meets an accident and required Rs Y lakhs for repairing.
Determine the amount that will be rebated by the insurance company.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(min(a, b))
