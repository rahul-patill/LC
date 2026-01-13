class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = []
        d = defaultdict(int)
        ans = 0
        pre = 0
        d[pre] += 1
        for i in nums:
            if i%2==1:
                pre += 1
            else:
                pre += 0
            prefix.append(pre)

            if (pre-k) in d:
                ans += d[pre-k]

            d[pre] += 1
        
        return ans