class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''if nums == []:
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
        
        return max(longest,a)+1'''
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest