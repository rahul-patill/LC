class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        s = []
        ans = []
        for i in range(len(prices) - 1, -1, -1):

            if s == []:
                s.append(prices[i])
                ans.append(s[-1])

            elif prices[i] < s[-1]:

                while s and prices[i] < s[-1]:
                    s.pop()

                if s:
                    ans.append(prices[i] - s[-1])
                elif s == []:
                    ans.append(prices[i])
                s.append(prices[i])

            elif prices[i] >= s[-1]:
                ans.append(prices[i] - s[-1])
                s.append(prices[i])

        return ans[::-1]
