class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1] % nums[0] == 0:
            return nums[0]
        maxi = 0
        for i in range(1,nums[0]):
            if nums[0] % i == 0 and nums[-1] % i == 0:
                maxi = max(maxi, i)
        return maxi
