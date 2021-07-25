# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from platform import node


class Solution:
    def hasCycle(self, head: node) -> bool:
        slowPoint = head
        fastPoint = head
        try:
            while True:
                slowPoint = slowPoint.next
                fastPoint = fastPoint.next.next
                if fastPoint == slowPoint:
                    return True
        except AttributeError:
            return False