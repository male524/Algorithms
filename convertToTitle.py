# 168. Excel Sheet Column Title
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""

class ConvertToTitle(object):
    def convertToTitle(self, n: int) -> str:
        result = ''
        while n != 0:
            result = chr(ord('A') + ((n - 1) % 26)) + result
            n = (n - 1) // 26
        return result

# I learned how to convert unicode into a character using the chr() function, and how to convert a string into unicode using the ord() function.
# By the way, this I didn't come up with the concept for this code, but I can explain what each part does. I really don't think this should be marked as an easy problem.