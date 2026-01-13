class Solution:
    # same as 560. Subarray Sum Equals K
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        prefix = []
        d = defaultdict(int)
        ans = 0
        pre = 0
        d[pre] += 1
        for i in nums:
            pre += i
            prefix.append(pre)

            if (pre-k) in d:
                ans += d[pre-k]

            d[pre] += 1
        
        return ans