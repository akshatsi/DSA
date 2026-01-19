class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''n = len(nums)
        for i in range(n//2+1):
            if nums[i] == target:
                return i 
            if nums[n-i-1] == target:
                return n-i-1
        return -1 '''

        low = 0 
        high = len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1