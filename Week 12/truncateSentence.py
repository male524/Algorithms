# 1816. Truncate Sentence
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = []
        words = s.split()
        for i in range(k):
            result.append(words[i])
            result.append(" ")
        return "".join(result[:-1])