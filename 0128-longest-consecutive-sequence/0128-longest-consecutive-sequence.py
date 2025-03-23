class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # finding the length of the list
        n = len(nums)
        if n == 0:
            return 0


        # putting everything into the set
        st = set()

        for i in nums:
            st.add(i)

        longest = -1


        # if you find the nest greater value in the set then add it to the count,
        # else just find the value which doesnt have the value below it  ||  ex: [2,3,4,5], so find 2






        for i in st:
            if (i-1) not in st:
                cnt = 1
                x = i

                while (x+1) in st:
                    x += 1
                    cnt += 1

                longest = max(longest, cnt)

        return longest
