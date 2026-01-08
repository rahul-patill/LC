class Solution:
    def findMin(self, nums: List[int]) -> int:

        # if only 1 element exist
        if len(nums) == 1:
            return nums[0]
        
        # if only 2 elements
        if len(nums) == 2:
            return min(nums[0],nums[1])


        start = 0
        end = len(nums) - 1

        # if array is already sorted
        if nums[start] <= nums[end]:
            return nums[start]

        # code starts
        while start <= end:

            mid = (start + end) // 2

            prev = (mid + len(nums) - 1) % len(nums)
            nextt = (mid + 1) % len(nums)
            if nums[prev] > nums[mid] and nums[mid] < nums[nextt]:
                return nums[mid]

            elif nums[0] <= nums[mid]:
                start = mid + 1

            else:
                end = mid - 1
