class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_dic = {}
        final = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diff_dic:
                return [diff_dic.get(nums[i]),i]
            diff_dic[diff] = i

            