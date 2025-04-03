class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pre = []
        suf = []
        vr = 0

        pre.append(0)
        for i in nums:
            vr = max(vr,i)
            pre.append(vr)
        
        print("pre",pre)
        pre.pop()



        vr = 0
        suf.append(0)
        for i in reversed(nums):
            vr = max(vr,i)
            suf.append(vr)
        suf.pop()
        suf = list(reversed(suf))
        print("suf",suf)
        reversed(nums)
        print("num",nums)


        ans = 0
        i=0
        for i in range(len(nums)):
            ans = max(ans, ( pre[i]-nums[i] ) * suf[i] )
        print(ans)
        return ans