# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from platform import node


class Solution:
    def removeNthFromEnd(self, head: node, n: int) -> node:
        l = head
        lLen = 1
        while l.next != None:
            l = l.next
            lLen += 1
        l = head
        delete = lLen - n - 1
        if delete == -1:
            try:
                head = head.next
                return head
            except AttributeError:
                pass
        for i in range(delete):
            l = l.next
        try:
            l.next = l.next.next
            return head
        except AttributeError:
            pass
