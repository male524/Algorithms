# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from platform import node


class Solution:
    def reverseList(self, head: node) -> node:
        l = head
        if head == None:
            return head
        while l.next:
            lnext = l.next
            l.next = l.next.next
            lnext.next = head
            head = lnext
        return head