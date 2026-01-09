class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        nums.sort()
        longest = 0
        a = 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                a += 1
                longest = max(longest, a)
            elif nums[i+1] == nums[i]:
                continue
            else:
                a = 0
        return longest+1