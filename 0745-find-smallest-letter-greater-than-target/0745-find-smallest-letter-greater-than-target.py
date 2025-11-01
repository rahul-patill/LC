class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        ans = letters[0]
        s, e = 0, len(letters) - 1

        

        while s<=e:
            mid = s +(e-s)//2
            # if letters[mid] == target:
            #     s = mid+1
            if letters[mid] > target:
                ans = letters[mid]
                e = mid-1
            elif (letters[mid]<=target):
                s = mid+1
            
        return ans

