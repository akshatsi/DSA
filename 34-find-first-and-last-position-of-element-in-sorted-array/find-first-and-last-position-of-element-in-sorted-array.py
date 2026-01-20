class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1,-1]
        n = len(nums)
        left = 0
        right = n-1
        while left <=right:
            if nums[left] == target and nums[right] == target:
                return[left,right]
            else:
                if nums[left]==target:
                    right -= 1
                elif nums[right] == target:
                    left += 1
                else:
                    left += 1
                    right -=1
        return [-1,-1]
           