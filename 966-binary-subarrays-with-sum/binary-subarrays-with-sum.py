class Solution:
    def atMostSum(self, nums: List[int], goal: int) -> int:
        total = 0
        l = 0
        r = 0
        curr_sum = 0
        if goal < 0:
            return 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum > goal:
                curr_sum -= nums[l]
                l += 1

            total += r - l + 1

        return total
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMostSum(nums, goal) - self.atMostSum(nums, goal - 1)