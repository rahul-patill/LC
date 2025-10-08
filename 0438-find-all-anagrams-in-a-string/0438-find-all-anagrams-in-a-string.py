class Solution:
    def findAnagrams(self, nums: str, pat: str) -> List[int]:
        # code here
        i,j = 0,0
        ans = []
        d = defaultdict(int)
        
        k = len(pat)
        
        
        
        for txt in pat:
            d[txt] += 1
            
        count = len(d)
        
        
        while (j<len(nums)):
            if nums[j] in pat:
                d[nums[j]] -= 1
                if d[nums[j]] == 0:
                    count -= 1
                
                
                
            if (j-i+1)<k :
                j+= 1
                
                
                
            elif (j-i+1) == k :
                if count == 0:
                    ans.append(i)
                
                if nums[i] in pat:
                    
                    if d[nums[i]] == 0:
                        count += 1
                        
                    d[nums[i]] += 1
                
                i += 1
                j+=1
                
                
                
                
        return ans