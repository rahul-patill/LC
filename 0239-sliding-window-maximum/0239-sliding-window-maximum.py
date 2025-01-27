class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = e = 0
        ans = []
        m = []
        n = len(nums)

        while e < n:
            # put first element if m is empty
            if len(m) == 0:
                m.append(nums[e])
            else:
                # keep removing until its the latest element is the largest
                while len(m) != 0 and m[-1] < nums[e]:
                    m.pop(-1)
                m.append(nums[e]) #anytime you are inserting the element 

            if (e - s + 1) < k:
                e += 1
            else:
                ans.append(m[0])

                if nums[s] == m[0]:
                    m.pop(0)

                e += 1
                s += 1
        return ans
