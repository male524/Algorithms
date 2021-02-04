# 1282. Group the People Given the Group Size They Belong To
"""
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

 

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
 

Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""

from typing import List


class GroupThePeople:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        numberOfLists = {}
        for i in groupSizes:
            if i not in numberOfLists:
                numberOfLists[i] = 1
            else:
                numberOfLists[i] += 1
        keysList = list(numberOfLists)
        valuesList = list(numberOfLists.values())
        for i in range(len(keysList)):
            valuesList[i] /= keysList[i]
            valuesList[i] = int(valuesList[i])
        finalList = []
        for i in range(len(valuesList)):
            x = valuesList[i]
            while x > 0:
                finalList.append([keysList[i]])
                x -= 1
        for i in range(len(groupSizes)):
            for j in range(len(finalList)):
                if len(finalList[j]) == finalList[j][0] + 1:
                    pass
                elif groupSizes[i] == finalList[j][0]:
                    finalList[j].append(i)
                    break
        for i in range(len(finalList)):
            finalList[i].pop(0)
        return finalList

# I learned how to index through a sublist (finalList = [[1,2,3],[4,5,6],[7,8,9]], finalList[1][0] would return 4). Other than that I just applied stuff I already knew, but it still took forever.
# It took me 1 hour and 37 minutes to finish this problem.