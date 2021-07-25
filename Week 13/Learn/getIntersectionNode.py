# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from platform import node


class Solution:
    def getIntersectionNode(self, headA: node, headB: node) -> node:
        A = headA
        B = headB
        lenA = lenB = 1
        if A == B:
            return A
        while A.next != None:
            A = A.next
            lenA += 1
        while B.next != None:
            B = B.next
            lenB += 1
        diff = abs(lenA - lenB)
        A = headA
        B = headB
        if lenA > lenB:
            for i in range(lenA):
                if A == B:
                    return A
                A = A.next
                if i >= diff:
                    B = B.next
        elif lenB > lenA:
            for i in range(lenB):
                if A == B:
                    return A
                B = B.next
                if i >= diff:
                    A = A.next
        else:
            for i in range(lenA):
                if A == B:
                    return A
                A = A.next
                B = B.next