class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        smallest = nums[0]
        left = 0
        while left < n:
            smallest = min(smallest, nums[left])
            left += 1

        return smallest