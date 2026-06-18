class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        low = 0
        high = 0 
        longest = 0
        zeros = 0
        while high < len(nums):
            if nums[high] == 0:
                zeros += 1

            while zeros > k:
                if nums[low] == 0:
                    zeros -= 1
                low += 1
            
            if zeros <= k:
                longest = max(longest, high - low + 1)

            high += 1

        return longest