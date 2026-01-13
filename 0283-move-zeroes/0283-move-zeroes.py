class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        end = len(nums)
        while j<end:

            if nums[j]!=0:
                nums[i] = nums[j]
                i+=1
            j+=1
        
        while i<end:
            nums[i] = 0
            i+=1
        