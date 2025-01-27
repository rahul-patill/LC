class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s = e = 0
        n = len(fruits)
        d = dict()
        ans  = 0

        if len(fruits) == 1:
            return 1

        while(e<n):
            d[fruits[e]] = d.get(fruits[e], 0) + 1

            
            if len(d) == 2  :
                ans = max(ans, e-s+1)

            elif (len(d) > 2):

                while len(d) > 2:
                    d[fruits[s]] -= 1
                    if d[fruits[s]] == 0:
                        del d[fruits[s]]
                
                    s+=1
            
            e+=1

        if len(d) == 1:
            return d[fruits[0]]
        
        return ans