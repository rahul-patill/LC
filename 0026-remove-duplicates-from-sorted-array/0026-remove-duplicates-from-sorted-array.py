class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        # for i in range(len(nums)-1):
        #     if ( nums[i] != nums[i+1] ):
        #         nums[k] = nums[i]
        #         k += 1        

        # if ( nums[k-1] != nums[len(nums)-1] ):
        #     nums[k] = nums[len(nums)-1]
        #     k+=1
        
        # return k


        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i
