class Solution5:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        shorterWord = None
        extra = str()
        if lenWord1 < lenWord2:
            shorterWord = word1
            extra = word2[len(word1):]
        elif lenWord2 < lenWord1:
            shorterWord = word2
            extra = word1[len(word2):]
        else:
            shorterWord = word1
        result = str()
        for i in range(len(shorterWord)):
            result += word1[i] + word2[i]
        result += extra
        return result