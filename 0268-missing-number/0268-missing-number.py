class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = int((n* (n+1) )/2)

        for i in nums:
            totalSum -= i
        
        return totalSum
