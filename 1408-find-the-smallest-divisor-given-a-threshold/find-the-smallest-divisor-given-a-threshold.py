class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def sum_check(divisor):
            total = 0
            for i in nums:
                total += math.ceil(i/divisor)
            return total <= threshold 
        low = 1
        high = max(nums)
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if sum_check(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res

