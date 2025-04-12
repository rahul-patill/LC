class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        mine = 5001
        while (s<=e):
            mid = floor(s + (e-s)/2)
            
            if (nums[s] <= nums[mid]):
                mine = min(mine, nums[s])
                s = mid+1
            else:
                mine = min(mine, nums[mid])
                e = mid-1
        
        return mine
