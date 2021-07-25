from operator import pos


class BTree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def preOrder(root: BTree):
    if root == None:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root: BTree):
    if root == None:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def postOrder(root: BTree):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)

postOrder(BTree(1,BTree(2),BTree(3,None,BTree(4))))