class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = 0
            for j in range(i+1, len(nums)):
                x = nums[i] + nums[j]
                if x == target:
                    return [i,j]