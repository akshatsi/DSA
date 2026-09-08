class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for idx, i in enumerate(nums):
            right -= i
            if right == left:
                return idx

            left += i

        return -1