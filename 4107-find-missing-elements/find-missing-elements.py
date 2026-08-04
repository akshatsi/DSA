class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        missing = []
        for i in range(mini, maxi):
            if i  not in nums:
                missing.append(i)

        return missing




