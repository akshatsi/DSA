class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            if nums[low] == nums[high] == target:
                return[low, high]
            else:
                if nums[low] == target and nums[high] != target:
                    high -= 1
                elif nums[high] == target and nums[low] != target:
                    low += 1

                else:
                    low += 1
                    high -= 1

        return [-1,-1]