class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)

        print(d)
        for i in d.keys():
            if d[i] == 1:
                return i

        
    