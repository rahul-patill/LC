class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        n = len(s)
        d = set()
        maxi = 0
        l = []
        while(j<n):
            l.append(s[j])
            d = set(l)
            if len(d) == len(l): #we can also use dict > j-i+1 condition and implement it
                maxi = max(maxi, len(l))
                j += 1
            elif len(d) < len(l):
                while(len(d) < len(l)):
                    l.pop(0)
                    i += 1
                j += 1
        return maxi