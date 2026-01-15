class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        
        print("dic : ", dic)
        for word in strs:
            alphaMap = [0] * 26
            for alphabet in word:
                alphaMap[ord(alphabet) - 97] += 1
            alphaMap = tuple(alphaMap)
            # tuple is used bcoz dictionary needs a key as tuple.
            # it cant use list as key, since its mutable


            dic[alphaMap].append(word)
        
        print(dic.values())
        
        return list(dic.values())
