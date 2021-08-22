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
    def inOrder(self, root: node):
        if root == None:
            return
        self.inOrder(root.left)
        self.result.append(root.val)
        self.inOrder(root.right)
    def inorderTraversal(self, root: node) -> List[int]:
        self.inOrder(root)
        return self.result