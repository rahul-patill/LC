class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans =  []
        s = set()
        for i in range(len(A)):
            temp = 0
            
            if A[i] in s:
                temp += 1
            else:
                s.add(A[i])
            
            if B[i] in s:
                temp += 1
            else:
                s.add(B[i])

            if ans:
                ans.append(ans[-1] + temp)
            else:
                ans.append(temp)
        
        return ans