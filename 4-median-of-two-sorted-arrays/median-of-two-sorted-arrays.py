class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1+nums2
        c.sort()
        if len(c) % 2 == 0:
            ans = (c[(len(c)//2)]+ c[(len(c)//2)-1])/2
            return ans
        else:
            return c[len(c)//2]