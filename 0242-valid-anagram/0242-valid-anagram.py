class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        dS = {}  #
        dT = {}  # dictionary for counting

        for i in range(len(s)):
            dS[s[i]] = 1 + dS.get(s[i], 0) #why used get() here, know
            dT[t[i]] = 1 + dT.get(t[i], 0)
        
        for j in dS:
            if dS[j] != dT.get(j): #why used only []      after used get()
                return False

        return True