# 20. Valid Parentheses
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution1:
    def isValid(self, s: str) -> bool:
        holder = []
        for i in range(len(s)):
            holder.append(s[i])
            if holder[-1] == ')' or holder[-1] == ']' or holder[-1] == '}':
                curChr = holder[-1]
                if curChr == ')':
                    revCurChr = str(chr(ord(curChr) - 1))
                else:
                    revCurChr = str(chr(ord(curChr) - 2))
                if revCurChr in holder:
                    first = len(holder) - 1 - holder[::-1].index(revCurChr)
                    second = len(holder) - 1 - holder[::-1].index(curChr)
                    dif = second - first
                    if dif > 1:
                        return False
                    holder.pop(second)
                    holder.pop(first)
                else:
                    return False
        if len(holder) > 0:
            return False
        else:
            return True

class Solution2:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        
print(Solution1.isValid(1, "(([{()}])())()[]{}"))
print(Solution2.isValid(1, "(([{()}])())()[]{}"))

# I learned how to get the index of the last item with a specific value in a list by doing len(list) - 1 - list[::-1].index(value)
# I looked at another person's solution and I learned what a stack is from it, so I included the code
# This one was really hard for me, it took me 3 hours