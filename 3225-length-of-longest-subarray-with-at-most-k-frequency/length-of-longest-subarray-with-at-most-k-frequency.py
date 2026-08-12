class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = {}
        res = 0
        low = 0
        for high in range(len(nums)):
            counter[nums[high]] = counter.get(nums[high], 0) + 1
            while counter[nums[high]] > k:
                counter[nums[low]] -= 1
                low += 1

            res = max(res, high - low + 1)

        return res