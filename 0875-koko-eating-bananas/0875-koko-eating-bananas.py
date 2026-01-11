class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(piles, h , mid):
            
            hours = 0
            for i in piles:
                hours += int(i/mid)

                if i%mid != 0:
                    hours +=1

                if hours>h:
                    return False
            
            if hours<=h:
                return True



        s = 1
        e = max(piles)
        ans = -1
        while s<=e:
            mid = (s+e)//2

            if canEat(piles, h , mid):
                ans = mid
                e = mid-1
            else:
                s =mid+1
        
        return ans

