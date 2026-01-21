class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        a = {}
        left = 0
        while left < len(nums):
            a[nums[left]] = a.get(nums[left],0)+1 
            left += 1

        return min(a,key=a.get)