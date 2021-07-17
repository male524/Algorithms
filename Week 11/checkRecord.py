# 551. Student Attendance Record I
class Solution6:
    def checkRecord(self, s: str) -> bool:
        row = 0
        rowCheck = False
        totalAbsent = 0
        for i in range(len(s)):
            if i == 0 and s[i] == 'L':
                row += 1
            elif i == 0 and s[i] != 'L':
                pass
            elif s[i] == 'L' and s[i-1] == 'L':
                row += 1
            elif s[i] == 'L' and s[i-1] != 'L':
                row += 1
            else:
                row = 0
            
            if row >= 3:
                rowCheck = True
            
            if s[i] == 'A':
                totalAbsent += 1
            
        if totalAbsent < 2 and rowCheck == False:
            return True
        else:
            return False