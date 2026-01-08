class Solution(object):
    def rearrangeArray(self, nums):
        ans = [0] * len(nums)
        pos,neg = 0,1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2
        return ans