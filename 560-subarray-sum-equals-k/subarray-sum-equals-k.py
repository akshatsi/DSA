class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''total = 0
        for i in range(len(nums)):  
            sum = 0
            for j in range(i,len(nums)):
                    sum += nums[j]
                    if sum == k:
                        total += 1
                    
        return total'''

        prefixSumCount = {}
        count = 0
        prefixSum = 0
        prefixSumCount[0] = 1
        for i in range(len(nums)):
            prefixSum += nums[i]
            remove = prefixSum - k
            if remove in prefixSumCount:
                count += prefixSumCount[remove]
            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1
        return count
