class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = []
        postfix= [0]*len(nums)

        pre = 0
        for i in nums:
            pre += i
            prefix.append(pre)
        
        print(prefix)

        post = 0
        for i in range(len(nums)-1,-1,-1):
            post += nums[i]
            postfix[i] = post
        print(postfix)


        for i in range(0,len(nums)):
            if prefix[i] == postfix[i]:
                return i
        
        if prefix[0] == postfix[0]:
            return 0

        elif prefix[len(nums)-1] == postfix[len(nums)-1]:
            return len(nums)-1
        else:
            return -1