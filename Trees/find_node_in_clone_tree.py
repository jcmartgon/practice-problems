# Jesus Carlos Martinez Gonzalez
# 26/07/2023
# Find a Corresponding Node of a Binary Tree in a Clone of That Tree (https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree)

"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        if not original or target == original:
            return cloned

        return self.getTargetCopy(
            original.left, cloned.left, target
        ) or self.getTargetCopy(original.right, cloned.right, target)
