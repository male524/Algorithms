# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tree1 = []
        self.tree2 = []
        self.which = True
    def traverse(self, root: Optional[TreeNode]):
        if root == None:
            return
        if self.which == True:
            self.tree1.append(root.val)
            self.traverse(root.left)
            self.traverse(root.right)
        else:
            self.tree2.append(root.val)
            self.traverse(root.left)
            self.traverse(root.right)
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root1)
        self.which = False
        self.traverse(root2)