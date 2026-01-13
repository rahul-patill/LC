class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        score = 0
        min_value = sum(nums)
        window_size = len(nums) - k

        if window_size == 0:
            return sum(nums)
        else:
            while j < len(nums):

                score += nums[j]
                # print("score", score)

                if (j - i + 1) < window_size:
                    j += 1
                elif (j - i + 1) == window_size:
                    min_value = min(score, min_value)
                    print("mini", min_value)
                    score -= nums[i]
                    i += 1
                    j += 1

            return sum(nums) - min_value
