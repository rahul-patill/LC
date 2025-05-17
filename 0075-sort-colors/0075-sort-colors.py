class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        m = 0
        h = n-1

        while(m<=h):
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1

            elif nums[m] == 1:
                m += 1
            else: # m == 2
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
        