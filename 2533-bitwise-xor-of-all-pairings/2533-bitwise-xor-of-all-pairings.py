class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        d = {}

        for i in nums1:
            if i in d:
                d[i] += len(nums2)
            else:
                d[i] = len(nums2)

        for i in nums2:
            if i in d:
                d[i] +=len(nums1)
            else:
                d[i] = len(nums1)

        ans  = []

        for key , value in d.items():
            if (value)%2 == 1:
                ans.append(key)

        count =  0
        for i in ans:
            count = count ^ i
        return count

