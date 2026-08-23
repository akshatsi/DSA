class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def div_sum(nums, div):
            total = 0
            for num in nums:
                total += math.ceil(num/div)

            return total

        
        low = 1
        high = max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if div_sum(nums, mid) <= threshold:
                ans = mid
                high = mid - 1
                
            else:
                low = mid + 1

        return ans