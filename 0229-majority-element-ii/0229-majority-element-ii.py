class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        mj1, mj2 = 0, 0
        c1, c2 = 0, 0
        result = []
        n = len(nums)

        for i in nums:

            if i == mj1:
                c1 += 1
            elif i == mj2:
                c2 += 1
            elif c1 == 0:
                mj1 = i
                c1+=1
            elif c2 == 0:
                mj2 = i
                c2+=1
            else:
                c1 -= 1
                c2 -= 1

        c1, c2 = 0, 0
        for i in nums:
            if i == mj1:
                c1 += 1
            elif i == mj2:
                c2 += 1

        if c1 > floor(n / 3):
            result.append(mj1)
        if c2 > floor(n / 3):
            result.append(mj2)

        return result
