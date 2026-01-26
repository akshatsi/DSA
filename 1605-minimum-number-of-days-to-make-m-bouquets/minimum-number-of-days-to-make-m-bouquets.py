class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def canMake(day):
            bouquets = 0
            flowers = 0

            for d in bloomDay:
                if d <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if canMake(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans