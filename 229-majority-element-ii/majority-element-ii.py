class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''a = len(nums)
        freq = {}
        for i in range (a):
            current = nums[i]
            if current in freq:
                freq[current]+= 1
                continue 
            freq[current] = 1   
        values = freq.values()
        result = []
        for i in values:
            if i > a/3:
                for key, value in freq.items():
                    if value == i:
                        result.append(key)
        return result'''
        a = len(nums)
        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            if value > a / 3:
                result.append(key)

        return result
                
        
