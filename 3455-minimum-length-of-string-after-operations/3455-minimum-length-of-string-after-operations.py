class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter(s)
        ans = 0 
    

        for key, value in d.items():
            if (value%2 == 0):
                ans += 2
            else:
                ans += 1
        
        return ans