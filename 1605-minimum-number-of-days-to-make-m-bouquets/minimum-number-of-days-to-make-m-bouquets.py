class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def canMake(days):
            bouquet = 0
            flowers = 0
            for d in bloomDay:
                if d <= days:
                    flowers += 1
                    if flowers == k:
                        bouquet += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquet >= m

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high)// 2
            if canMake(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
