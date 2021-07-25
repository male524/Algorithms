# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from platform import node


class Solution:
    def removeElements(self, head: node, val: int) -> node:
        if head == None:
            return head
        l = head
        while l.next:
            if l.next.val == val:
                l.next = l.next.next
            else:
                l = l.next
        if head.val == val:
            head = head.next
        return head