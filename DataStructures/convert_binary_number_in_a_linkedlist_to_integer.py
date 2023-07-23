# Jesus Carlos Martinez Gonzalez
# 22/07/2023
# Convert binary number in a linkedlist to integer (https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer)

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = 0

        while head:
            number = (number << 1) | head.val
            head = head.next

        return number
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = 0

        while head:
            number = (number << 1) | head.val
            head = head.next

        return number
