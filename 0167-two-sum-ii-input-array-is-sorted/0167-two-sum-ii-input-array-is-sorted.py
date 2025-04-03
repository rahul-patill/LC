class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        
        # solution using two pointer
        l, r = 0, len(num) - 1

        while l<r:
            curSum = num[l] + num[r]

            if curSum > target:
                r-=1
            elif curSum < target:
                l+=1
            else:
                return [l+1, r+1]
            