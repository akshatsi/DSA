class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range (0,n-1 ):
            b = nums[i]
            c = i
            for j in range(i ,n):
                if nums[j]<b:
                    b = nums[j]
                    c = j   
                else:
                    continue     
            x = nums[i]            
            nums[i] = nums[c]
            nums[c] = x