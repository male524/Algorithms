# 744. Find Smallest Letter Greater Than Target
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        temp = []
        for i in range(len(letters)):
            temp.append(ord(letters[i]))
        if ord(target) >= max(temp):
            return chr(min(temp))
        return min(i for i in letters if ord(i) > ord(target))