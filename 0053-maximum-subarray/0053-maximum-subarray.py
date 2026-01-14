class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = 0
        result = -10001

        for i in nums:
            if ans >=0:
                ans += i
                print("+", ans)
            else:
                ans = i
                print("-", ans)
            
            result = max(result, ans)
        
        return result
