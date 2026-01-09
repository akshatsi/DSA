class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            nums.sort()
        longest = 0
        a = 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                a += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                longest = max(longest, a)
                a = 0               
        
        return max(longest,a)+1