class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] != 1:
                count = 0
                continue
            count += 1
            maxi = max(maxi, count)
        return maxi