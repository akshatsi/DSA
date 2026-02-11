class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        subsets = 1 << n #total num of subsets (2 ** n)
        for num in range(subsets):
            subset = []
            for i in range (n):
                if num & (1 << i):
                    subset.append(nums[i])
            ans.append(subset)

        return ans 

