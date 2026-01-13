class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        prefix = []
        ans = 0
        for i in nums:
            ans += i
            prefix.append(ans)
        return prefix