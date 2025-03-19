class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        print(s)

        ans = ''
        s.reverse()
        for i in s :
            if i == "":
                continue
            
            ans += i
            ans += " " 
        
        return ans.strip()
         
        