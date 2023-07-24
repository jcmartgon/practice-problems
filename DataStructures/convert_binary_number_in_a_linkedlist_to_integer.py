# Jesus Carlos Martinez Gonzalez
# 22/07/2023
# Convert binary number in a linkedlist to integer (https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer)

"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
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
