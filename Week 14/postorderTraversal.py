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
    def postOrder(self, root: node):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.result.append(root.val)
    def postorderTraversal(self, root: node) -> List[int]:
        self.postOrder(root)
        return self.result