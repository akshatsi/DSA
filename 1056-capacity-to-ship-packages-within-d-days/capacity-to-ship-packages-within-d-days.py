class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysC(weights: List[int], cap: int) -> int:
            days_used = 1
            current = 0
            for w in weights:
                if current + w <= cap:
                    current += w
                else:
                    days_used += 1
                    current = w

            return days_used

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if daysC(weights, mid) <= days:
                right = mid - 1   # try smaller capacity
            else:
                left = mid + 1    # need larger capacity

        return left