class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(weights, days, mid):
            value = 0
            # Start with 1 day, because we are currently loading the 1st day
            count = 1 
            for i in weights:
                value += i

                if value > mid:
                    count += 1
                    value = i

                if count > days:
                    return False

            # If total days needed is <= allowed days, this capacity works
            if count <= days:
                return True

        if len(weights) < days:
            return False
        else:
            s = max(weights)
            e = sum(weights)
            res = -1
            print(s, e)

            while s <= e:
                mid = (s + e) // 2
                if canShip(weights, days, mid):
                    res = mid
                    e = mid - 1
                else:
                    s = mid + 1
            return res
