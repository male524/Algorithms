# 7. Reverse Integer
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""

class Reverse:
    def reverse(self, x: int) -> int:
        strInt = str(x)
        revIntList = []
        if x < 0:
            for i in range(len(strInt)):
                if strInt[i] > strInt[0]:
                    revIntList.append(strInt[-i])
            revIntList.insert(0, strInt[0])
        else:
            for i in range(1, len(strInt) + 1):
                revIntList.append(strInt[-i])
        revInt = ""
        for i in range(len(revIntList)):
            revInt += revIntList[i]
        revInt = int(revInt)
        if revInt > 2 ** 31 - 1 or revInt < -2 ** 31:
            return 0
        else:
            return revInt

# I used things that I've already learned to solve this one.
# It took me longer than I'd like to admit... it took me probably around an hour and a half.
# I had trouble with checking if the input number was too big or too small.
# It turned out I had a little order of operations typo and a typo in the variable my code was checking, I kept checking the wrong variable.