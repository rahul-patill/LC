class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = e = 0
        n = len(nums)
        sum = 0
        ans = float("inf")

        while(e<n):
            sum += nums[e]

            if (sum >= target):
                ans = min(ans, e-s+1)
                print(e, s)
                while(sum >= target):
                    sum -= nums[s]
                    s+=1
                    if sum>=target:
                        ans = min(ans, e-s+1)
                
            
            e+=1
        if (ans == float("inf")):
            return 0
        return ans


