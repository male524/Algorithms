# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from platform import node


class Solution:
    def __init__(self):
        self.leftList = []
        self.rightList = []
        self.first = True
    def left(self, root: node):
        if root == None:
            self.leftList.append([])
            return
        if self.first == True:
            self.first = False
            self.left(root.left)
        else:
            self.leftList.append(root.val)
            self.left(root.left)
            self.left(root.right)
    def right(self, root: node):
        if root == None:
            self.rightList.append([])
            return
        if self.first == True:
            self.first = False
            self.right(root.right)
        else:
            self.rightList.append(root.val)
            self.right(root.right)
            self.right(root.left)
    def isSymmetric(self, root: node) -> bool:
        self.left(root)
        self.first = True
        self.right(root)
        if self.leftList == self.rightList:
            return True
        else:
            return False