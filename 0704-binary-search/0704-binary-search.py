class Solution:
    def search(self, nums: List[int], target: int) -> int:

        s, e = 0, len(nums) - 1

        while s <= e:
            mid = (s + (e - s) // 2)  
# Use (s + e) // 2 in Python since integers don’t overflow, but use s + (e - s) // 2            in interviews or other languages to prevent integer overflow when computing the midpoint.

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                e = mid - 1
            elif target > nums[mid]:
                s = mid + 1

        return -1