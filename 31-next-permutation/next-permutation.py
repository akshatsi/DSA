class Solution(object):
    def nextPermutation(self, nums):
        fixed = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                fixed = i
                break

        if fixed == -1:
            nums.reverse()
            return

        for i in range(len(nums) - 1, fixed, -1):
            if nums[i] > nums[fixed]:
                nums[i], nums[fixed] = nums[fixed], nums[i]
                break

        nums[fixed + 1:] = reversed(nums[fixed + 1:])