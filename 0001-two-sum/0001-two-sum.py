class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}  # //dict for storing all the key and values in it

        # key = items of nums
        # values = index of nums wrt items

        ans = []  # list for storing all the answer

        # for item in nums:
        #     x = target - item
        #     if x in storage:
        #         ans.append(storage[x])
        #         ans.append(nums.index(item))
        #         return ans
        #     else:
        #         storage[item] = nums.index(item)
        
        # over here if you use like the above one, you get do not get the index of values in list
        # if there are multiple values
        # ex: see example 3 in the description ; so good to use index thing




        for i in range(len(nums)): 
            x = target - nums[i]

            if x in storage :
                ans.append(storage[x])
                ans.append(i)
                return ans
            else : 
                storage[nums[i]] = i



# think what you would do if :
# 1.input is sorted
# 2.unsorted