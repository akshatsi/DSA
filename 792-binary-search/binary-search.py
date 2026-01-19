class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n//2+1):
            if nums[i] == target:
                return i 
            if nums[n-i-1] == target:
                return n-i-1
        return -1
