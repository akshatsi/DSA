class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        res = float('inf')   
        sum = 0
        while high < len(nums):
            sum += nums[high]
            while sum >= target:
                res = min(res, (high - low + 1))
                sum -= nums[low]
                low += 1
            high += 1

        return res if res < float('inf') else 0
            

        


        