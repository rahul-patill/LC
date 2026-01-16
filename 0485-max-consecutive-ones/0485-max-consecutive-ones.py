class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        i = 0
        j =0
        ones = 0
        ans = 0
        while j<len(nums):
            
            if nums[j] == 1:
                
                ans = max(j-i+1,ans)
            else:
                i = j
                if i+1<len(nums):
                    i+=1
            j+=1
        return ans