class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) % 2:
            return True

        for num in nums1:
            if num % 2:
                return False
            
        
        return True