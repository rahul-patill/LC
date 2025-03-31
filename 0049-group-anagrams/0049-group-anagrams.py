class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for word in strs:
            alphaMap = [0] * 26
            for alphabet in word:
                alphaMap[ord(alphabet) - 97] += 1
            alphaMap = tuple(alphaMap)
            dic[alphaMap].append(word)
        
        print(dic.values())
        
        return list(dic.values())
