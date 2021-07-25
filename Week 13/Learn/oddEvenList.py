# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from platform import node


class Solution:
    def oddEvenList(self, head: node) -> node:
        if head == None: 
            return head
        head2 = head.next
        cur = head
        nxt = head2
        while nxt:
            cur.next = nxt.next
            if nxt.next:
                nxt.next = nxt.next.next
            if cur.next:
                cur = cur.next
            nxt = nxt.next
        cur.next = head2
        return head