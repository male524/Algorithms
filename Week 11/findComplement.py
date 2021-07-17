# 476. Number Complement
class Solution2:
    def findComplement(self, num: int) -> int:
        bnum = list(bin(num)[2:])
        for i in range(len(bnum)):
            if bnum[i] == '1':
                bnum[i] = '0'
            else:
                bnum[i] = '1'
        
        return int(''.join(bnum), 2)