class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def canBloom(bloomDay, m, k, mid):
            count = 0
            b = 0

            for i in bloomDay:
                if i <= mid:
                    count += 1
                else:
                    count = 0

                if count == k:
                    b += 1
                    count = 0

                if b == m:
                    return True
            return False

        # code starts here
        if (m * k) > len(bloomDay):
            return -1
        else:

            s = min(bloomDay)
            e = max(bloomDay)
            ans = -1
            while s <= e:
                mid = (s + e) // 2
                print(mid)
                if canBloom(bloomDay, m, k, mid):
                    ans = mid
                    e = mid - 1
                else:
                    s = mid + 1
            return ans
