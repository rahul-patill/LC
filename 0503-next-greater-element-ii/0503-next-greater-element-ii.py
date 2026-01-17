class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        nums2 = nums+nums
        print("nums2",nums2)

        ans = []
        s = []
        # finding greater for nums2
        for i in range(len(nums2) - 1, -1, -1):
            if not s:
                ans.append(-1)

            elif nums2[i] < s[-1]:
                ans.append(s[-1])

            elif nums2[i] >= s[-1]:
                while len(s) != 0 and nums2[i] >= s[-1]:
                    s.pop(-1)
                if len(s) == 0:
                    ans.append(-1)
                else:
                    ans.append(s[-1])

            s.append(nums2[i])

        ans.reverse()
        print("ans",ans)
        return ans[:len(nums)]