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
        self.firstHalf = True
    def level(self, root: node):
        pass
    def levelOrder(self, root: node) -> List[List[int]]:
        self.level(root)