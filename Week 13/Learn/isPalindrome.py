# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from platform import node


class Solution:
    def isPalindrome(self, head: node) -> bool:
        notrev = []
        l = head
        while l:
            notrev.append(l.val)
            l = l.next
        rev = notrev
        rev = list(rev)
        rev.reverse()
        if notrev == rev:
            return True
        return False