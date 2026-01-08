class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        s = 0
        e = len(nums) - 1

        while s < e and nums[s] == nums[s + 1]:
            s += 1
        
        while s < e and nums[e - 1] == nums[e]:
            e -= 1

        while s <= e:
            mid = floor(s + (e - s) / 2)

            if nums[mid] == target:
                return True

            # s sorted
            if nums[s] <= nums[mid]:
                if nums[s] <= target and target <= nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1

            # e sorted
            else:
                if nums[mid] <= target and target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1
        return False