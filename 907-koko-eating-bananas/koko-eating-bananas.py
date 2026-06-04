class Solution:
    def totalHours(self, piles: List[int], speed: int) -> int:
        totalH = 0
        for banana in piles:
            totalH += math.ceil(banana/speed)
        return totalH

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = max(piles)
        while low <= high:
            mid = (low + high) // 2
            totalH = self.totalHours( piles, mid)
            if totalH <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans