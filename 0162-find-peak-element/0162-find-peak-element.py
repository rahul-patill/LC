class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1

        if(len(nums) == 1 ):
            return 0

        # if(len(nums) == 2):
        #     if(nums[0] > nums[1]):
        #         return 0
        #     else:
        #         return 1



        while(s<=e):
            
            mid = floor(s + (e-s)/2)
            

            # if found
            if ((mid>0) and (mid<len(nums)-1)):
                if (nums[mid-1] < nums[mid]  and nums[mid]>nums[mid +1] ):
                    return mid
            

                #  if 4<5
                if(nums[mid] < nums[mid+1]):
                    s = mid +1
            
                # 5 > 4
                elif (nums[mid] > nums[mid +1 ]):
                    e = mid-1
            

            # if mid at 0
            if(mid == 0):
                if (nums[mid] > nums[mid+1]):
                    return 0
                else:
                    return 1 #why this?
            
            # if mid at last
            if (mid == len(nums) -1):
                if (nums[mid-1] < nums[mid]):
                    return len(nums)-1
                else:
                    return len(nums)-2

