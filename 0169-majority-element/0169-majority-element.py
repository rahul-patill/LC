class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = floor(len(nums)/2)
        ans = 0
        for i in d:
            print(n)
            if d[i]>n:
                ans = i
        return ans