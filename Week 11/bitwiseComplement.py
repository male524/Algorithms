# 1009. Complement of Base 10 Integer
class Solution1:
    def bitwiseComplement(self, n: int) -> int:
        bnum = list(bin(n)[2:])
        for i in range(len(bnum)):
            if bnum[i] == '1':
                bnum[i] = '0'
            else:
                bnum[i] = '1'
        
        return int(''.join(bnum), 2)