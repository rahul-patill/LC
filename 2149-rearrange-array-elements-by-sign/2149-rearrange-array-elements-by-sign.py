class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        ans = []
        for i in nums:
            print(i)
            if (i>0):
                positive.append(i)
            else:
                negative.append(i)
        print(positive,"+" ,negative)
        for i in range(0, len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        
        return ans