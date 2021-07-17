# 1550. Three Consecutive Odds
from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                counter += 1
            else:
                counter = 0
            if counter >= 3:
                return True
        return False