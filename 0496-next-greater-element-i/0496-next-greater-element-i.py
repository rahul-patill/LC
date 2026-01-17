class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []
        s = []

        for i in range(len(nums2) - 1, -1, -1):
            if not s:
                ans.append(-1)

            elif nums2[i] < s[-1]:
                ans.append(s[-1])
            
            elif nums2[i] > s[-1]:
                while len(s) != 0 and nums2[i] > s[-1]:
                    s.pop(-1)
                if len(s) == 0:
                    ans.append(-1)
                else:
                    ans.append(s[-1])

            s.append(nums2[i])

        ans.reverse()
        print(ans)


        d = defaultdict(int)
        for i in range(0, len(nums2)):
            d[nums2[i]] = ans[i]
        
        print(d)

        result = []
        for i in nums1:
            result.append(d[i])
        
        return result