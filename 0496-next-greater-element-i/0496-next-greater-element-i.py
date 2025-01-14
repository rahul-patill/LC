class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # first fir nge for nums 2 and store it in dict


        # declaring
        stack = []  # which is a list
        d = {}  # dictionary

        for e in nums2[::-1]:
            # if stack is empty for the last element
            if (stack == []):
                d[e] = -1
            
            
            # if element if there in stack and element < stack top, so put in dictionary
            elif ( e < stack[-1] ):
                d[e] = stack[-1]
            
            
            # if element if there in stack and element < stack top, so pop till 1)it becomes empty or 2)found element > stack top
            elif (e > stack[-1]):
                while ( len(stack)>0 and (e > stack[-1])  ) :
                    stack.pop()

                if  stack == []:
                    d[e] = -1
                elif (e < stack[-1]):
                    d[e] = stack[-1]

            stack.append(e)
        

        # now put value in list for the nums , using dictionary for nums 2

        ans = []
        for e in nums1:
            ans.append(d[e])
        
        return ans

            

