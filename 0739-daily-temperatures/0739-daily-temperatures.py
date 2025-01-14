class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:

        s = []
        ans = []

        for i in range(len(temps) - 1, -1, -1):

            if s == []:
                ans.append(0)

            elif temps[i] >= s[-1][0]:

                while s and temps[i] >= s[-1][0] :
                    s.pop(-1)

                if s:
                    ans.append(s[-1][1] - i)
                else:
                    ans.append(0)

            elif temps[i] < s[-1][0] :
                ans.append(s[-1][1] - i)

            s.append((temps[i], i))


        return ans[::-1]