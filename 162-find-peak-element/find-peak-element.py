class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''n = len(nums) 
        left = 0
        right = n-1
        while left <= right:
            if nums[left] < nums[right]:
                left += 1
            elif left == right:
                return left
            else:
                right -= 1'''
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid+1
        return left