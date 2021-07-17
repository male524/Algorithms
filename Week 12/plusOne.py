# 66. Plus One
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        return [i for i in str(int("".join(digits)) + 1)]