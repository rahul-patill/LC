class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        i, j = 0, 0
        d = defaultdict(int)
        size = 0

        while j < len(nums):

            d[nums[j]] += 1
            print(nums[j])

            if len(d) == j - i + 1:
                size = max(size, j - i + 1)
                j += 1
            elif len(d) < j - i + 1:
                while len(d) < j - i + 1:
                    d[nums[i]] -= 1
                    if d[nums[i]] == 0:
                        d.pop(nums[i])
                    i+=1
                j += 1

        return size
