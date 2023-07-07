# Jesus Carlos Martinez Gonzalez
# 06/07/2023
# Merge two sorted linkedlists (https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem)

"""
Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. 
Either head pointer may be null meaning that the corresponding list is empty.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the mergeLists function below.


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    new_head = SinglyLinkedListNode(0)
    curr = new_head

    if head1 == None:
        return head2
    if head2 == None:
        return head1

    while head1 and head2:
        if head1.data <= head2.data:
            curr.next = SinglyLinkedListNode(head1.data)
            head1 = head1.next
        else:
            curr.next = SinglyLinkedListNode(head2.data)
            head2 = head2.next

        curr = curr.next

    if head1 == None:
        curr.next = head2
    if head2 == None:
        curr.next = head1

    return new_head.next


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, " ", fptr)
        fptr.write("\n")

    fptr.close()
