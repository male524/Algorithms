# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from platform import node
from typing import List


class Solution:
    def __init__(self):
        self.result = []
    def preOrder(self, root: node):
        if root == None:
            return
        self.result.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
    def preorderTraversal(self, root: node) -> List[int]:
        self.preOrder(root)
        return self.result