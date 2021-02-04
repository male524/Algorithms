# 709. To Lower Case
"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in str])

