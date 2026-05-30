class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = minProd = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            curr = nums[i]
            if curr < 0:
                maxProd , minProd = minProd, maxProd
            maxProd = max(curr, maxProd * curr)
            minProd = min(curr, minProd * curr)

            res = max(res, maxProd)

        return res

            







