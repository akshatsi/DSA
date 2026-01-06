class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = {}
        for i in nums:
            total[i] = total.get(i,0)+1
            
        c = max(total, key = total.get)
        return c
        