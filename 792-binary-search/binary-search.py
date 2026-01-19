class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''n = len(nums)
        for i in range(n//2+1):
            if nums[i] == target:
                return i 
            if nums[n-i-1] == target:
                return n-i-1
        return -1 '''

        left = 0 
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right -= 1
            elif nums[mid] < target:
                left += 1
                
        return -1