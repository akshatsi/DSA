class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        res = len(nums)  
        total = 0
        while high < len(nums):
            total += nums[high]
            while total >= target:
                res = min(res, (high - low + 1))
                total -= nums[low]
                low += 1
            high += 1

        return res if sum(nums) >= target else 0
            

        


        