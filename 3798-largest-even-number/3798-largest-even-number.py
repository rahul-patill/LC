class Solution:
    def largestEven(self, s: str) -> str:
        
        index = -1
        for i in range(len(s)-1,-1,-1):
            if s[i] == '2':
                index = i
                break
        
        if index == -1:
            return ""
        else:
            return s[:index+1]
