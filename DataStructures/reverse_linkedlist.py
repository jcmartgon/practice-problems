# Jesus Carlos Martinez Gonzalez
# 23/07/2023
# Reverse linkedlist (https://leetcode.com/problems/reverse-linked-list)

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        if head:
            new_head = ListNode(head.val)

            curr = head.next
            while curr:
                new_head = ListNode(curr.val, new_head)
                curr = curr.next

        return new_head
