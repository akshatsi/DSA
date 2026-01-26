class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        if len(nums) > threshold:
            return -1

        def checker(nums, div):
            return sum(math.ceil(x / div) for x in nums)

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2

            if checker(nums, mid) <= threshold:
                right = mid - 1     
            else:
                left = mid + 1      

        return left