# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from platform import node


class Solution:
    def detectCycle(self, head: node) -> node:
        fast = slow = head
        try:
            while True:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    slow = head
                    while True:
                        if fast == slow:
                            return fast
                        slow = slow.next
                        fast = fast.next
        except AttributeError:
            return None