# 1736. Latest Time by Replacing Hidden Digits
class Solution8:
    def maximumTime(self, time: str) -> str:
        newTime = list(time)
        index = [i for i in range(len(newTime)) if newTime[i] == '?']
        for i in range(len(time)):
            if i in index:
                if i == 0:
                    if time[1] != '?':
                        if int(time[1]) < 4:
                            newTime[0] = '2'
                        else:
                            newTime[0] = '1'
                    else:
                        newTime[0] = '2'
                elif i == 1:
                    if time[0] == '0' or time[0] == '1':
                        newTime[1] = '9'
                    else:
                        newTime[1] = '3'
                elif i == 3:
                    newTime[3] = '5'
                elif i == 4:
                    newTime[4] = '9'
                
        return ''.join(newTime)