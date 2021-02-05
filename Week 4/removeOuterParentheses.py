# 1021. Remove Outermost Parentheses
"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        SList = []
        removeList = []
        nestCount = 0
        for i in range(len(S)):
            SList.append(S[i])
        for i in range(len(SList)):
            if SList[i] == '(':
                if nestCount == 0:
                    removeList.append(i)
                    nestCount += 1
                else:
                    nestCount += 1
            elif SList[i] == ')':
                if nestCount == 1:
                    removeList.append(i)
                    nestCount -= 1
                else:
                    nestCount -= 1
        removeList.reverse()
        for i in range(len(removeList)):
            SList.pop(removeList[i])
        return ''.join(SList)

print(Solution.removeOuterParentheses(0, "(()())(())(()(()))"))

# I learned how to use the reverse() function to reverse the order of a list.
# This took me around 25 minutes