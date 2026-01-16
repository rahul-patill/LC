class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find [i-1]<[i]:

        gola_index = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i-1]<nums[i]:
                gola_index = i-1
                break

        if gola_index != -1:
            swap_index = -1
            for i in range(len(nums) - 1, -1, -1):
                if nums[i]>nums[gola_index]:
                    swap_index = i
                    break
            
            nums[gola_index], nums[swap_index] = nums[swap_index], nums[gola_index]

        nums[gola_index+1 : len(nums)] = nums[gola_index+1 : len(nums)][::-1]




