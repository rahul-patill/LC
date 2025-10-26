class Solution:
    def findMin(self, nums: List[int]) -> int:


        if nums[0] <= nums[len(nums)-1]:
            return nums[0]

        s = 0
        e = len(nums)-1
        while (s<e):

            mid = (s + (e-s)//2)
            
            if nums[mid] > nums[e]:
                s = mid+1
            else:
                e = mid
        
        return nums[s]

