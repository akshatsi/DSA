class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_seen = {}

        for index in range(len(nums)):
            current = nums[index]
            needed = target - current

            if needed in numbers_seen:
                return [numbers_seen[needed], index]

            numbers_seen[current] = index