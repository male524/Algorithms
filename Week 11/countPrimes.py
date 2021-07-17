# 204. Count Primes
import math

class Solution3:
    def countPrimes(self, n: int) -> int:
        n_list = [True for i in range(n+1)]
        for i in range(n+1):
            if i >= math.sqrt(n):
                break
            elif n_list[i] == True:
                if i >= 2:
                    j = i ** 2
                    while j <= n:
                        n_list[j] = False
                        j += i
        n_list = n_list[2:]
        try:
            if n_list[-1] == True:
                return n_list.count(True) - 1
            else:
                return n_list.count(True)
        except IndexError:
            return 0