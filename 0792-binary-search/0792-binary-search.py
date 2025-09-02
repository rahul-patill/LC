class Solution:
    def search(self, nums: List[int], target: int) -> int:

        s, e = 0, len(nums) - 1

        while s <= e:
            mid = floor(s + (e - s) / 2)

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                e = mid - 1
            elif target > nums[mid]:
                s = mid + 1

        return -1
