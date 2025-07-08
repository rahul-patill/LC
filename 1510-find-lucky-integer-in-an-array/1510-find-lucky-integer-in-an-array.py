class Solution:
    def findLucky(self, arr: List[int]) -> int:
        highestValue = -1
        dic = dict(Counter(arr))

        for key in dic:
            if key == dic[key]:
                highestValue = max(highestValue, key)
        
        return highestValue