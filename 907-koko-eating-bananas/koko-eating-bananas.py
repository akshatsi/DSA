class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(piles,speed):
            totalH = 0
            for bananas in piles:
                totalH += math.ceil(bananas/speed)

            return totalH
        low = 1
        high = max(piles)
        ans = max(piles)

        while low <= high:
            mid = (low + high) // 2
            totalH = totalTime(piles,mid)
            if totalH <= h:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1


        return ans
