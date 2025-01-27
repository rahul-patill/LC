class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        s = e = 0
        n = len(string)
        d = dict()
        ans = 0

        while e < n:
            d[string[e]] = d.get(string[e], 0) + 1

            # if window is greater than len(dictionary)
            if (e - s + 1) > len(d):
                d[string[s]] -= 1

                if d[string[s]] == 0:
                    del d[string[s]]

                s += 1

            # if window is equal to len(dictionary)
            elif (e - s + 1) == len(d):
                ans = max(ans, e - s + 1)

            e += 1

        return ans
