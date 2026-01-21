class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums) 
        left = 0
        right = n-1
        while left <= right:
            if nums[left] < nums[right]:
                left += 1
            elif left == right:
                return left
            else:
                right -= 1