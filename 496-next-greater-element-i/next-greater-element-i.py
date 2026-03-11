class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = [0] * len(nums1)

        # Step 1: Precompute next greater for nums2
        next_greater = [0] * len(nums2)
        stack = []

        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()
            if not stack:
                next_greater[i] = -1
            else:
                next_greater[i] = nums2[stack[-1]]
            stack.append(i)

        # Step 2: Map nums2 elements to their next greater
        map_ = {}
        for i in range(len(nums2)):
            map_[nums2[i]] = next_greater[i]

        # Step 3: Build result using nums1
        for i in range(len(nums1)):
            result[i] = map_[nums1[i]]

        return result