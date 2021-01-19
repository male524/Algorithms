# 1684. Count the Number of Consistent Strings
"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
"""

from typing import List


class CountConsistentStrings:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        TFConstStr = []
        allowedChars = []
        result = 0
        for i in words:
            TFConstStr.append(True)
        char = ord("a")
        for i in range(26):
            for j in allowed:
                if ord(j) == char:
                    ordOf = ord(j)
            if "ordOf" in locals():
                if ordOf == char:
                    pass
                else:
                    allowedChars.append(char)
            else:
                allowedChars.append(char)
            char += 1
        for i in range(len(words)):
            for j in range(len(words[i])):
                for k in allowedChars:
                    if ord(words[i][j]) == k:
                        TFConstStr[i] = False
                    else:
                        pass
        for i in range(len(TFConstStr)):
            if TFConstStr[i] == True:
                result += 1
        return result