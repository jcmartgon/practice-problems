# Jesus Carlos Martinez Gonzalez
# 01/09/2023
# Pass the exam (https://www.codechef.com/problems/PASSTHEEXAM)

"""
Chef appeared for an exam consisting of 3 sections. Each section is worth 100 marks.
Chef scored A marks in Section 1, B marks in section 2, and C marks in section 3.
Chef passes the exam if both of the following conditions satisfy:
• Total score of Chef is > 100:
• Score of each section > IO.
Determine whether Chef passes the exam or not.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("PASS" if a + b + c >= 100 and a >= 10 and b >= 10 and c >= 10 else "FAIL")
