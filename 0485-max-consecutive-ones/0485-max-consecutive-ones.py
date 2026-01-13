class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        i = 0
        j =0
        ones = 0
        ans = 0
        while j<len(nums):
            
            if nums[j] == 1:
                ones+=1
                ans = max(ones,ans)
            else:
                i=j
                ones = 0
                if i<len(nums):
                    i+=1
            j+=1
        return ans