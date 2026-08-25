class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        '''res = float('inf')
        if k not in nums:
            return k
        for i in range(0,len(nums)):
            if nums[i] % k == 0:
                res = min(res, nums[i])

        while res in nums:
            if res + k not in nums:
                return res + k
            res+= k '''
            

        num = set(nums)
        i = 1
        while True:
            if i * k not in num:
                return i *k
            else:
                i += 1