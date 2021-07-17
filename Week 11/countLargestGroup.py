class Solution:
    def countLargestGroup(self, n: int) -> int:
        sumList = list()
        for i in range(1,n + 1):
            temp = i
            total = 0
            while temp > 0:
                digit = temp % 10
                total = total + digit
                temp = temp // 10
            sumList.append(total)
        countList = list()
        fCheck = list()
        for i in sumList:
            if i not in fCheck:
                count = sumList.count(i)
                countList.append(count)
                fCheck.append(i)
        return countList.count(max(countList))

print(Solution.countLargestGroup(None,15))