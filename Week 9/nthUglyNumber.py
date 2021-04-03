# 264. Ugly Number II
"""
Given an integer n, return the nth ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is typically treated as an ugly number.
 

Constraints:

1 <= n <= 1690
Accepted
203,141
Submissions
472,639
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result = [1]
        p2 = p3 = p5 = 0
        for i in range(1,n):
            result.append(min(result[p2] * 2, result[p3] * 3, result[p5] * 5))
            if result[p2] * 2 == result[i]:
                p2 += 1
            if result[p3] * 3 == result[i]:
                p3 += 1
            if result[p5] * 5 == result[i]:
                p5 += 1
        return max(result)