class Solution:
    def numAtmostSubarrays(self, nums: List[int], k: int) -> int:
        l = 0 
        r = 0
        total = 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                k -= 1
            while k < 0:
                if nums[l] % 2 != 0:
                    k+=1
                l += 1
            total += r - l + 1
                

        return total
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.numAtmostSubarrays(nums, k) - self.numAtmostSubarrays(nums, k-1)
                
                