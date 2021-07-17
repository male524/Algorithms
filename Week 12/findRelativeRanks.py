# 506. Relative Ranks
from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        placement = []
        copy = score
        for i in range(len(score)):
            index = copy.index(max(copy))
            placement.append(index)
            copy[index] = -1
        result = [0] * len(placement)
        print(placement)
        for i in range(len(placement)):
            if i == 0:
                result[placement[i]] = "Gold Medal"
            elif i == 1:
                result[placement[i]] = "Silver Medal"
            elif i == 2:
                result[placement[i]] = "Bronze Medal"
            else:
                result[placement[i]] = str(i+1)
        return result

print(Solution.findRelativeRanks(None, [123123,11921,1,0,123]))