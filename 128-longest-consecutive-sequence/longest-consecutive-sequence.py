class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()

        count = 1
        maxi = 1

        for i in range(0, len(nums) -1):
            if nums[i+1] - nums[i] == 1:
                count += 1
                maxi = max(maxi, count)
            elif nums[i+1] == nums[i]:
                continue
            else:
                count = 1

        return maxi