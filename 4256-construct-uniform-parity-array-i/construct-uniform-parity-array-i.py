class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        '''if not nums1 or len(nums1) == 1:
            return True

        nums2 = [0] * len(nums1)
        j = 1

        for i in range(len(nums1)):
            if i % 2 == 1:
                nums2[i] = nums1[i]
            else:
                nums2[i] = nums1[i] - nums1[j]

        odd = 0
        even = 0

        for x in nums2:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1

        return odd == 0 or even == 0'''
        return True