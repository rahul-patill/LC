class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set() #storing the duplicate triplet
        result = []

        for i in range(0, len(nums)-2):
            l = i+1
            r = len(nums)-1

            while l<r:
                if nums[i]+nums[l]+nums[r] == 0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l+=1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r-=1
        
        for items in ans:
            print((items))
            result.append((items))
        
        return result
