# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from platform import node


class Solution:
    def __init__(self):
        self.temp = 0
        self.max = 0
    def depth(self, root: node):
        if root == None:
            return
        self.temp += 1
        if self.temp > self.max:
            self.max = self.temp
        self.depth(root.left)
        self.depth(root.right)
        self.temp -= 1
    def maxDepth(self, root: node) -> int:
        if root == None:
            return 0
        self.depth(root)
        return self.max