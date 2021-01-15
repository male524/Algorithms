# 1281. Subtract the Product and Sum of Digits of an Integer
"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
"""

from functools import reduce

class SubtractProductAndSum(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        listN = []
        n = str(n)
        for i in n:
            listN.append(int(i))
        PoD = reduce((lambda x, y : x * y), listN)
        SoD = sum(listN)
        diff = PoD - SoD
        return diff

# I learned how to use the math.prod() function to multiply all items in a list, but I didn't use it here since it wouldn't work even when I imported "math".
# I also learned how to use lambda, at least sort of. I also learned how to use the reduce() function from functools (I decided to go with this method because it worked when I imported the library on leetcode.)