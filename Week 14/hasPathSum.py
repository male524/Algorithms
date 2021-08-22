# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from platform import node


class Solution:
    def __init__(self):
        self.sum = int()
        self.check = False
        self.first = True
    def path(self, root: node, target):
        if root == None:
            return
        self.sum += root.val
        if root.left == None and root.right == None:
            if self.sum == target:
                self.check = True
        self.path(root.left, target)
        self.path(root.right, target)
        self.sum -= root.val
    def hasPathSum(self, root: node, targetSum: int) -> bool:
        self.path(root, targetSum)
        if self.check == True:
            return True
        else:
            return False