class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        '''smallest = nums[0]
        left = 0
        while left < n:
            smallest = min(smallest, nums[left])
            left += 1

        return smallest''' #easy approach, with 100% no binary search needed

        low = 0
        high = n -1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]