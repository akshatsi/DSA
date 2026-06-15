class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = [0] * len(nums1)
        nextGreater = [0] * len(nums2)
        stack = []
        for i in range(len(nums2) -1, -1,-1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            
            if not stack:
                nextGreater[i] = -1

            else:
                nextGreater[i] = stack[-1]

            stack.append(nums2[i])

        map_ = {}
        for i in range (len(nums2)):
            map_[nums2[i]] = nextGreater[i]

        for i in range(len(nums1)):
            result[i] = map_[nums1[i]]

        return result
