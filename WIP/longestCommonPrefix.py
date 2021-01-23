# 14. Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def lookahead(iterable):
            it = iter(iterable)
            last = next(it)
            for val in it:
                yield last, True
                last = val
            yield last, False
        
        result = ''
        end = False
        if len(strs) == 0:
            return result
        for i in range(len(strs) - 1):
            if len(strs) == 1:
                end = True
                break
            elif strs[i] == strs[i + 1]:
                end = True
            else:
                end = False
        if end == True:
            result += strs[0]
            return result
        for i, more1 in lookahead(range(len(min(strs, key = len)))):
            for j in range(len(strs) - 1):
                if strs[j][i] == strs[j + 1][i]:
                    pass
                else:
                    return result
            result += strs[0][i]
            if more1 == False:
                return result
     
print(Solution.longestCommonPrefix(1, ["ab", "a", "abcdefg", "a"]))