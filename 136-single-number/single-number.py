class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            count ^= nums[i]

        return count